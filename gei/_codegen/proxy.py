"""Ce que toute classe générée a en commun — écrit une fois, pour tous.

UNE CLASSE GÉNÉRÉE ENVELOPPE UNE `dsviper.Value`, ELLE NE LA COPIE PAS. La donnée vit dans
la Value ; la classe lui donne des noms. Tout ce qui découle de ça — l'égalité, le hachage,
la lecture de la valeur enveloppée — ne dépend d'aucun type du modèle, donc rien de tout
cela n'a à être émis une fois par type.

ET IL FAUT UNE BASE COMMUNE, PAS SEULEMENT PARCE QUE C'EST PLUS COURT. La liaison Python ne
relie pas `dsviper.ValueStructure` à `dsviper.Value` à l'exécution : `isinstance(v,
dsviper.Value)` est faux pour toute valeur concrète, alors que le `.pyi` déclare
`class ValueStructure(Value)`. Il n'y a donc aucun moyen de reconnaître une valeur du
runtime par son type ; reconnaître *nos* classes est le seul test qui tienne, et il demande
qu'elles aient un ancêtre.
"""

from __future__ import annotations

import typing

import dsviper


class Proxy:
    """Une valeur du modèle, nommée.

    L'ÉGALITÉ PORTE SUR LA VALEUR ET SUR LA CLASSE. `ModelA::Colour` et `ModelB::Colour`
    enveloppent des Values de types différents, donc la comparaison de valeurs suffirait ;
    exiger la même classe le dit quand même, parce que c'est ce qui est voulu et non ce qui
    se trouve être vrai.
    """

    __slots__ = ("_value",)

    def __init__(self, value):
        self._value = value

    @property
    def vpr_value(self):
        """La valeur du runtime. C'est la donnée ; la classe n'en est que la lecture."""
        return self._value

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self._value == other._value

    def __hash__(self) -> int:
        return self._value.hash()

    def encode(self, **kwargs) -> dsviper.ValueBlob:
        return dsviper.Value.encode(self._value, **kwargs)

    def copy(self):
        return type(self)(self._value.copy())

    def __lt__(self, other) -> bool:
        return self._value < unwrap(other)

    def __le__(self, other) -> bool:
        return self._value <= unwrap(other)

    def __gt__(self, other) -> bool:
        return self._value > unwrap(other)

    def __ge__(self, other) -> bool:
        return self._value >= unwrap(other)

    def hexdigest(self) -> str:
        return dsviper.Value.hexdigest(self._value)

    # ── le passage, dans les deux sens ──
    #
    # UN SEUL COUPLE DE NOMS POUR TOUT CE QUI A UNE CLASSE. Une structure et une clé sont des
    # `Proxy` ; une énumération est une `enum.Enum` de Python et n'en est pas une. Sans un
    # protocole commun, le code généré devrait savoir laquelle des deux il tient — donc
    # porter dans le template une distinction que le modèle connaît déjà.

    @classmethod
    def _wrap(cls, value) -> typing.Self:
        return cls(value)

    def _unwrap(self):
        return self._value


# ── la table des classes du modèle ──
#
# UNE VALEUR CONNAÎT SON TYPE, ET UN TYPE NOMMÉ CONNAÎT SON IDENTIFIANT D'EXÉCUTION. Il ne
# manque donc qu'une table qui dise quelle classe va avec quel identifiant, et chaque unité
# la remplit en une ligne pour les types qu'elle déclare. C'est ce qui permet à un conteneur
# de rendre ses éléments avec leurs noms sans qu'aucune classe de conteneur soit générée :
# le pack en émet une par combinaison rencontrée, ici il n'y en a aucune.

class _Neuf:
    """Le témoin d'un argument absent, là où `None` est une valeur possible."""

    def __repr__(self) -> str:
        return "<neuf>"


NEUF = _Neuf()

_CLASSES: dict[str, type] = {}

# LES DÉFINITIONS DU MODÈLE, POSÉES PAR LE PAQUET. Décoder demande de savoir quel modèle lire,
# et une vue générique ne peut pas le deviner — c'est la seule chose que le socle emprunte au
# paquet qui l'accueille, et il la reçoit au chargement.
_DEFINITIONS = None


def set_definitions(definitions) -> None:
    global _DEFINITIONS
    _DEFINITIONS = definitions


def definitions_of():
    if _DEFINITIONS is None:
        raise RuntimeError("le paquet n'a pas déclaré ses définitions")
    return _DEFINITIONS()


def register(classes: dict) -> None:
    """Déclarer les classes d'une unité, par l'identifiant d'exécution de leur type."""
    for runtime_id, cls in classes.items():
        _CLASSES[runtime_id.encoded()] = cls


def wrap(value) -> typing.Any:
    """La valeur du runtime, rendue avec les noms du modèle quand il y en a.

    RENDUE `Any`, ET C'EST UNE DÉCISION PLUTÔT QU'UN RENONCEMENT. Le type réel dépend de ce
    que la valeur porte, donc il ne peut pas être écrit ici ; mais il est écrit à chaque
    endroit qui appelle -- une propriété annotée `Sequence[Colour]`, un pool annoté
    `MaterialKey`. Le vérificateur y trouve un type exact. Ce qu'on concède est un point de
    passage, déclaré une fois, au lieu d'un `Any` répandu sur chaque champ.

    CE QUI N'A PAS DE NOM PASSE TEL QUEL, et c'est le cas de tous les types primitifs : le
    runtime rend déjà un `int`, un `str`, un `float`. Ce qui en a un -- une structure, une
    clé, une énumération -- reçoit sa classe. Ce qui en contient d'autres reçoit une vue qui
    enveloppe en lisant.
    """
    code = getattr(value, "type_code", None)
    if code is None:
        return value

    code = code()
    if code == "struct" or code == "enum":
        return _named(value.type())._wrap(value)

    if code == "key":
        return _named(value.type_concept())(value)

    if code in ("optional", "any"):
        return None if value.is_nil() else wrap(value.unwrap())

    if code == "variant":
        return wrap(value.unwrap())

    from .container import Mapping, Ordered, Sequence

    if code == "map":
        return Mapping(value)
    if code == "xarray":
        return Ordered(value)
    if code in ("vector", "set", "vec", "mat", "tuple"):
        return Sequence(value)

    return value


def _named(type_):
    """La classe de ce type, ou une erreur qui dit laquelle manque.

    ÉCHOUER PLUTÔT QUE RENDRE LA VALEUR NUE. L'appelant est un accesseur annoté `Colour` ou
    `Sequence[Colour]` ; lui rendre une `ValueStructure` serait un mensonge que le typage ne
    peut pas rattraper, et qui se découvrirait bien plus loin, sur un attribut absent. Un type
    sans classe veut dire qu'une unité n'a pas été importée -- ou qu'une fonctionnalité n'a pas
    été sélectionnée -- et l'erreur le nomme.

    C'est le contrat de viper : une valeur du mauvais type est rejetée là où elle apparaît, et
    non plus loin. `raise` et non `assert`, pour que ça tienne aussi sous `python -O`.
    """
    cls = _CLASSES.get(type_.runtime_id().encoded())
    if cls is None:
        raise TypeError(
            f"aucune classe générée pour {type_.representation()} : "
            f"l'unité qui le déclare n'est pas importée")
    return cls


def is_known(value) -> bool:
    """Le modèle connaît-il le concept que cette clé désigne ?

    LA TABLE RÉPOND, ET C'EST LA MÊME QUESTION. Une unité y enregistre les types qu'elle
    déclare ; un identifiant d'exécution absent est donc celui d'un concept qu'aucune unité
    chargée ne porte -- un descendant venu d'ailleurs, ou une unité non importée. Le pack
    répond en comparant à une liste figée à la génération ; ici la réponse suit ce qui est
    réellement chargé.
    """
    return value.type_concept().runtime_id().encoded() in _CLASSES


def unwrap(value) -> typing.Any:
    """La Value que le runtime attend, depuis ce que l'appelant a écrit.

    Ce qui n'est pas une de nos classes passe tel quel : `Value.loads` du runtime sait déjà
    convertir un objet Python depuis le descripteur de type, donc un `int`, un `str` ou un
    `dict` n'a besoin de rien ici. Un conteneur Python est déplié élément par élément, parce
    qu'il peut en contenir qui, eux, ont une classe.
    """
    if hasattr(value, "_unwrap"):
        return value._unwrap()
    if isinstance(value, (list, tuple)):
        return [unwrap(element) for element in value]
    if isinstance(value, set):
        return {unwrap(element) for element in value}
    if isinstance(value, dict):
        return {unwrap(key): unwrap(element) for key, element in value.items()}
    return value


class AnyConceptKey(Proxy):
    """Une clé sur une instance de n'importe quel concept.

    LE C++ EN GÉNÈRE UNE PAR MODÈLE ; ICI IL N'EN FAUT AUCUNE. Elle ne nomme aucun type :
    elle enveloppe un `ValueKey` et pose ses questions au descripteur que la valeur porte
    déjà. Ce qu'une version générée y ajoutait — savoir nommer les concepts du modèle — est
    dans les définitions embarquées, lues à l'exécution, ce qui la rend juste aussi pour un
    descendant apparu après la génération.
    """

    __slots__ = ()

    def __init__(self, value: dsviper.ValueKey):
        if not isinstance(value, dsviper.ValueKey):
            raise TypeError("cette valeur n'est pas une clé")
        super().__init__(value)

    def instance_id(self) -> dsviper.ValueUUId:
        return self._value.instance_id()

    def runtime_id(self) -> dsviper.ValueUUId:
        return self._value.type_concept().runtime_id()

    def is_valid(self) -> bool:
        return self._value.instance_id().is_valid()

    def description(self) -> str:
        """L'instance et le concept qu'elle désigne, dits comme le modèle les nomme."""
        return (f"{self._value.instance_id().encoded()}:AnyConceptKey"
                f"({self._value.type_concept().representation()}Key)")

    def is_known(self) -> bool:
        return is_known(self._value)

    @classmethod
    def decode(cls, blob, definitions=None, **kwargs) -> "AnyConceptKey":
        return cls(dsviper.ValueKey.cast(dsviper.Value.decode(
            blob, dsviper.TypeKey(dsviper.TypeAnyConcept()),
            definitions if definitions is not None else definitions_of(), **kwargs)))

    def as_(self, cls):
        """La clé vue comme celle d'un concept donné, ou `None` si elle n'en est pas une."""
        return cls(self._value) if self._value.type() == cls.type() else None

    def __repr__(self) -> str:
        return self.description()
