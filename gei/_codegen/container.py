"""Les conteneurs, rendus avec les noms du modèle — écrits une fois, pour tous.

CE QUE LE PACK GÉNÈRE ICI, ET POURQUOI IL N'Y A RIEN À GÉNÉRER. Le pack Python émet une classe
par forme de conteneur rencontrée : `Optional_Colour`, `Vector_Parts_Colour`,
`Map_Core_ThingKey_to_Parts_ThingKey`, une par combinaison, soit environ 700 des 1 259 lignes
de son `data.py.stg`. Or `Optional_Colour` et `Optional_int32` ne diffèrent que par deux
choses : le descripteur du type, et la classe qui enveloppe un élément.

Et ces deux choses, la valeur les porte déjà. Une `Value` connaît son type, et un type nommé
connaît son identifiant d'exécution ; il suffit donc d'une table qui dise quelle classe va
avec quel identifiant, et d'une vue qui enveloppe en lisant. Une unité enregistre ses classes
en une ligne, et aucune combinaison n'a plus à être prévue -- y compris celles qu'un modèle
ajoutera ensuite.

UNE VUE ET NON UNE COPIE. La donnée reste dans la Value : `c.f_vector[0]` construit un
`Colour` au moment où on le demande, et `c.f_vector.append(…)` écrit dans la Value.

ET LA SURFACE EST CELLE DU RUNTIME, PAS UNE SÉLECTION. Mesuré sur la suite d'épreuves du
projet : une vue qui n'offrait que la lecture faisait échouer 301 de ses 474 tests, parce que
l'usage réel construit, mute, copie, sérialise et positionne. Ce qui suit transmet tout ce que
la valeur sous-jacente sait faire ; ne transmettre qu'une partie, c'était choisir à la place
de l'appelant.
"""

from __future__ import annotations

import typing

import dsviper

from .proxy import definitions_of as _definitions, unwrap, wrap

E = typing.TypeVar("E")
K = typing.TypeVar("K")


class View:
    """Ce que les quatre vues ont en commun, et qui vient de la Value.

    Le type, l'encodage, la copie, l'empreinte : aucun ne dépend de la forme du conteneur. Ce
    sont des questions posées à la valeur, et la vue ne fait que les transmettre — une vue
    obtenue d'un champ doit y répondre comme une vue construite par son nom, puisque c'est la
    même valeur derrière.
    """

    __slots__ = ("_value",)

    # DÉCLARÉ, ET PAS SEULEMENT AFFECTÉ. Une sous-classe qui définit `__getattr__` fait douter
    # le vérificateur de tout attribut résolu autrement ; l'annotation dit lequel existe.
    _value: typing.Any

    def __init__(self, value):
        self._value = value

    @property
    def vpr_value(self):
        return self._value

    def _unwrap(self):
        return self._value

    def type(self):
        return self._value.type()

    def copy(self):
        return type(self)(self._value.copy())

    def encode(self, **kwargs):
        return dsviper.Value.encode(self._value, **kwargs)

    def hexdigest(self) -> str:
        return dsviper.Value.hexdigest(self._value)

    def __eq__(self, other) -> bool:
        """COMPARER À N'IMPORTE QUOI EST LÉGITIME, et la réponse est « non ».

        `x in [1, 2, "trois"]` compare à chaque élément ; laisser le runtime lever sur un type
        qu'il ne connaît pas transformerait une question en erreur, et `in` deviendrait
        impraticable.
        """
        other_value = other.vpr_value if isinstance(other, View) else other
        if not hasattr(other_value, "type_code") and not isinstance(
                other_value, (list, tuple, set, dict)):
            # NE PAS DEMANDER AU RUNTIME CE QU'IL NE PEUT PAS RÉPONDRE. Comparer une suite à un
            # entier le fait lever, et une exception posée au niveau C survit à un `except` :
            # l'interpréteur rend alors « un résultat avec une exception en attente », et `in`
            # devient impraticable. Écarter avant l'appel est le seul endroit sûr.
            return NotImplemented
        try:
            return bool(self._value == other_value)
        except (TypeError, ValueError, dsviper.ViperError):
            return False

    def __hash__(self) -> int:
        return self._value.hash()

    def __repr__(self) -> str:
        return repr(self._value)


class Sequence(View, typing.Generic[E]):
    """Une suite du runtime — vector, set, vec, tuple — dont les éléments portent leurs noms."""

    __slots__ = ()

    def __len__(self) -> int:
        return len(self._value)

    def __iter__(self) -> typing.Iterator[typing.Any]:
        # UNE MAT N'EST PAS ITÉRABLE, et toutes les autres suites le sont. L'index est le seul
        # accès que les quatre portent ; itérer par lui marche partout.
        if hasattr(self._value, "__iter__"):
            return (wrap(element) for element in self._value)

        # UNE MATRICE EST UNE SUITE DE COLONNES, et non une suite de nombres. Son `at` prend
        # deux rangs, et la parcourir à plat perdrait sa forme -- ce que le modèle dit d'elle.
        type_ = self._value.type()
        if hasattr(type_, "columns"):
            columns, rows = type_.columns(), type_.rows()
            return (tuple(wrap(self._value.at(column, row)) for row in range(rows))
                    for column in range(columns))
        return (wrap(self._value.at(index)) for index in range(len(self._value)))

    def __getitem__(self, index) -> E:
        # UNE MATRICE S'INDEXE PAR DEUX RANGS. `m[1, 2]` passe un tuple, que la valeur attend
        # sous forme de deux arguments.
        if isinstance(index, tuple):
            return wrap(self._value.at(*index))
        return wrap(self._value[index])

    def __setitem__(self, index: int, element: E) -> None:
        self._value[index] = unwrap(element)

    def __contains__(self, element) -> bool:
        return unwrap(element) in self._value

    def at(self, *position) -> E:
        # UNE MATRICE S'INDEXE PAR COLONNE ET PAR LIGNE, les autres suites par un seul rang.
        # La vue transmet ce qu'on lui donne plutôt que de choisir une arité.
        return wrap(self._value.at(*position))

    def append(self, element: E) -> None:
        # UNE SUITE N'EST PAS TOUJOURS UN VECTEUR. Un ensemble ajoute par `add`, un vecteur par
        # `append`, et un vec ne grandit pas du tout. La vue transmet au nom que la valeur
        # connaît plutôt que d'imposer le sien.
        if hasattr(self._value, "append"):
            self._value.append(unwrap(element))
        else:
            self._value.add(unwrap(element))

    def add(self, element: E) -> None:
        self.append(element)

    def insert(self, index: int, element: E) -> None:
        self._value.insert(index, unwrap(element))

    def extend(self, elements) -> None:
        for element in elements:
            self.append(element)

    def pop(self, *args) -> E:
        return wrap(self._value.pop(*args))

    def remove(self, element: E) -> None:
        self._value.remove(unwrap(element))

    def discard(self, element: E) -> None:
        self._value.discard(unwrap(element))

    def index(self, element: E):
        return self._value.index(unwrap(element))

    def count(self, element: E) -> int:
        return self._value.count(unwrap(element))

    def contains(self, element: E) -> bool:
        return self._value.contains(unwrap(element))

    def clear(self) -> None:
        self._value.clear()

    def empty(self) -> bool:
        return self._value.empty()

    def size(self) -> int:
        return len(self._value)

    def to_list(self) -> list[E]:
        return list(self)

    def to_tuple(self) -> tuple:
        return tuple(self)

    def __add__(self, other):
        return type(self)(self._value + unwrap(other))

    def __iadd__(self, other):
        self._value += unwrap(other)
        return self

    def __getattr__(self, name: str):
        """`get_0` pour un tuple, et tout ce que la valeur porte sans que la vue le nomme.

        LA VUE NE CHOISIT PAS CE QUI PASSE. Un ensemble a `isdisjoint`, `issubset`, `min`,
        `max`, `intersection_update` ; un vecteur en a d'autres ; les nommer un par un
        reviendrait à recopier le runtime et à se périmer au premier ajout. Ce qui est
        transmis est enveloppé au retour, ce qui est passé est déballé -- c'est tout ce que la
        vue ajoute.
        """
        if name.startswith("get_") and name[4:].isdigit():
            return lambda _i=int(name[4:]): self[_i]
        return _forward(self, name)

    # Les opérations d'ensemble, transmises telles que la valeur les porte.
    def union(self, other):
        return type(self)(self._value.union(unwrap(other)))

    def intersection(self, other):
        return type(self)(self._value.intersection(unwrap(other)))

    def difference(self, other):
        return type(self)(self._value.difference(unwrap(other)))

    def update(self, other) -> None:
        self._value.update(unwrap(other))

    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.difference(other)

    def __ior__(self, other):
        self._value.update(unwrap(other))
        return self

    def __iand__(self, other):
        self._value.intersection_update(unwrap(other))
        return self

    def __isub__(self, other):
        self._value.difference_update(unwrap(other))
        return self

    def symmetric_difference(self, other):
        return type(self)(self._value.symmetric_difference(unwrap(other)))

    def __xor__(self, other):
        return self.symmetric_difference(other)

    def __ixor__(self, other):
        # LE RUNTIME N'A PAS TOUJOURS LA FORME EN PLACE. Quand elle manque, la composer depuis
        # celle qui rend une valeur dit la même chose sans rien inventer.
        if hasattr(self._value, "symmetric_difference_update"):
            self._value.symmetric_difference_update(unwrap(other))
            return self
        return type(self)(self._value.symmetric_difference(unwrap(other)))


class Mapping(View, typing.Generic[K, E]):
    """Une map du runtime, dont les clés et les valeurs portent leurs noms."""

    __slots__ = ()

    def __len__(self) -> int:
        return len(self._value)

    def __iter__(self) -> typing.Iterator[K]:
        return (wrap(key) for key in self._value)

    def __getitem__(self, key: K) -> E:
        return wrap(self._value.at(unwrap(key)))

    def __setitem__(self, key: K, element: E) -> None:
        self._value.set(unwrap(key), unwrap(element))

    def __delitem__(self, key: K) -> None:
        del self._value[unwrap(key)]

    def __contains__(self, key: K) -> bool:
        return unwrap(key) in self._value

    def at(self, key: K) -> E:
        return wrap(self._value.at(unwrap(key)))

    def set(self, key: K, element: E) -> None:
        self._value.set(unwrap(key), unwrap(element))

    def get(self, key: K, default=None):
        return wrap(self._value.get(unwrap(key), unwrap(default))) if default is not None \
            else (wrap(self._value.at(unwrap(key))) if unwrap(key) in self._value else None)

    def setdefault(self, key: K, element: E) -> None:
        self._value.setdefault(unwrap(key), unwrap(element))

    def pop(self, key: K, *args) -> E:
        return wrap(self._value.pop(unwrap(key), *[unwrap(a) for a in args]))

    def remove(self, key: K) -> None:
        self._value.remove(unwrap(key))

    def discard(self, key: K) -> None:
        self._value.discard(unwrap(key))

    def contains(self, key: K) -> bool:
        return self._value.contains(unwrap(key))

    def update(self, other) -> None:
        self._value.update(unwrap(other))

    def clear(self) -> None:
        self._value.clear()

    def empty(self) -> bool:
        return self._value.empty()

    def size(self) -> int:
        return len(self._value)

    def __getattr__(self, name: str):
        return _forward(self, name)

    def keys(self) -> list[K]:
        return list(self)

    def values(self) -> list[E]:
        return [self[key] for key in self]

    def items(self) -> list[tuple[K, E]]:
        return [(key, self[key]) for key in self]


class Ordered(View, typing.Generic[E]):
    """Un xarray du runtime : une suite dont chaque place a une identité stable.

    LA POSITION EST LA CLÉ, ET C'EST TOUT CE QUI LE DISTINGUE D'UN `vector`. Deux éditeurs qui
    insèrent au même endroit n'écrasent pas l'insertion l'un de l'autre, parce que chaque
    élément est désigné par un identifiant et non par un rang. La vue expose donc les positions
    autant que les éléments -- les masquer reviendrait à en faire un vecteur.
    """

    __slots__ = ()

    END = dsviper.ValueXArray.END

    @staticmethod
    def end() -> dsviper.ValueUUId:
        """La position d'après le dernier, là où insérer pour ajouter à la fin."""
        return dsviper.ValueXArray.END

    def __len__(self) -> int:
        return len(self._value)

    def __iter__(self) -> typing.Iterator[E]:
        return (wrap(element) for element in self._value)

    def __getitem__(self, key) -> E:
        return wrap(self._value[key])

    def __setitem__(self, key, element: E) -> None:
        self._value[key] = unwrap(element)

    def __delitem__(self, key) -> None:
        del self._value[key]

    def __contains__(self, element) -> bool:
        return unwrap(element) in self._value

    @staticmethod
    def create_position() -> dsviper.ValueUUId:
        return dsviper.ValueXArray.create_position()

    def positions(self) -> list[dsviper.ValueUUId]:
        return self._value.positions()

    def position(self, index: int):
        return self._value.position(index)

    def index(self, position: dsviper.ValueUUId):
        return self._value.index(position)

    def position_of(self, element):
        """La position du premier élément égal, ou `None`.

        `position` prend un rang, celle-ci prend une valeur. Le pack les distingue par le nom,
        et c'est le bon choix : un rang et un élément ne se confondent pas.
        """
        for position in self.positions():
            if self.at(position) == element:
                return position
        return None

    def has_position(self, position: dsviper.ValueUUId) -> bool:
        return self._value.has_position(position)

    def at(self, position: dsviper.ValueUUId):
        element = self._value.at(position)
        return None if element is None else wrap(element)

    def set(self, position: dsviper.ValueUUId, element: E) -> None:
        self._value.set(position, unwrap(element))

    def insert(self, before_position, element: E, new_position=None):
        return self._value.insert(before_position, unwrap(element), new_position) \
            if new_position is not None else self._value.insert(before_position, unwrap(element))

    def insert_position(self, before_position, new_position) -> None:
        self._value.insert_position(before_position, new_position)

    def append(self, element: E):
        return self._value.append(unwrap(element))

    def remove(self, position: dsviper.ValueUUId) -> None:
        self._value.remove(position)

    def items(self) -> list[tuple[dsviper.ValueUUId, E | None]]:
        """Les paires position/élément, dans l'ordre.

        LA POSITION EST CE QUI FAIT UN XARRAY, donc la lire séparément de l'élément oblige à
        deux parcours et à supposer qu'ils s'alignent. Une seule liste le dit.
        """
        # LA FIN N'EST PAS UNE PLACE. `positions()` la rend parce qu'on y insère ; la compter
        # comme une paire ferait un élément de plus à chaque parcours.
        return [(position, self.at(position)) for position in self.positions()
                if position != dsviper.ValueXArray.END]

    def __getattr__(self, name: str):
        return _forward(self, name)

    def to_vector(self):
        """Le xarray à plat, comme un vecteur — et du type que le modèle lui donne.

        `Sequence` nue perdrait le lien au type : un appelant qui compare à `Vector_int8`
        cherche la classe liée, pas la vue générique.
        """
        return sequence_of(self._value.to_vector().type)(self._value.to_vector())

    def empty(self) -> bool:
        return len(self._value) == 0

    def size(self) -> int:
        return len(self._value)


class Optional(View, typing.Generic[E]):
    """Une valeur, ou rien.

    UNE VUE À ELLE, ET NON UNE SUITE. Un `optional` a une question qu'aucun autre conteneur ne
    pose -- « y a-t-il quelque chose ? » -- et trois opérations qui en découlent. Les lire
    comme une suite de zéro ou un élément compilerait et ne dirait rien de juste.

    Les accesseurs générés, eux, rendent `None` plutôt qu'un `Optional` : `None` est ce que
    Python a pour dire l'absence, et une classe pour ça n'apporterait que du poids. Cette vue
    sert quand on tient l'optional lui-même — construit par son nom, ou lu comme valeur.
    """

    __slots__ = ()

    def __bool__(self) -> bool:
        return not self.is_nil()

    def is_nil(self) -> bool:
        return self._value.is_nil()

    def unwrap(self) -> E:
        return wrap(self._value.unwrap())

    def wrap(self, element: E) -> None:
        self._value.wrap(unwrap(element))

    def get(self, default=None):
        if self.is_nil():
            return wrap(default) if default is not None else None
        return self.unwrap()

    def clear(self) -> None:
        self._value.clear()


class Variant(View, typing.Generic[E]):
    """L'une de plusieurs alternatives, et celle qui est tenue.

    Comme l'optional, une vue à elle : la question est « laquelle ? », et elle n'a de sens pour
    aucune autre forme.
    """

    __slots__ = ()

    def unwrap(self) -> E:
        return wrap(self._value.unwrap())

    def wrap(self, element, type=None) -> None:
        self._value.wrap(unwrap(element), type) if type is not None \
            else self._value.wrap(unwrap(element))

    def __getattr__(self, name: str):
        """`set_<alternative>`, `get_<alternative>`, `is_<alternative>`.

        LE PACK EN ÉMET TROIS PAR ALTERNATIVE DE CHAQUE VARIANT DU MODÈLE. Le type du variant
        connaît ses alternatives : l'objet répond au nom demandé s'il en désigne une, et lève
        sinon en disant lesquelles existent.
        """
        for prefix in ("set_", "get_", "is_"):
            if not name.startswith(prefix):
                continue
            wanted = name[len(prefix):]
            for alternative in self._value.type().types():
                if _alternative_name(alternative) != wanted:
                    continue
                if prefix == "set_":
                    return lambda value, _t=alternative: self._value.wrap(unwrap(value), _t)
                if prefix == "get_":
                    def taken(_t=alternative):
                        held = self._value.unwrap(encoded=False)
                        if held.type() != _t:
                            raise ValueError(
                                f"le variant tient un {held.type().representation()}, "
                                f"pas un {_t.representation()}")
                        return wrap(held)

                    return taken
                return lambda _t=alternative: self._value.unwrap(encoded=False).type() == _t

        known = ", ".join(_alternative_name(t) for t in self._value.type().types())
        raise AttributeError(f"'{name}' ne désigne aucune alternative : {known}")


# ── un conteneur nommé, et constructible ──
#
# CE QUE LA VUE SEULE NE DONNAIT PAS. Une vue enveloppe la valeur d'un champ qui existe déjà ;
# elle ne permet pas d'écrire `Vector_uint8([1, 2, 3])`, donc pas de construire un conteneur
# pour le passer à une fonction de pool, ni de bâtir un document avant de l'attacher. Mesuré
# sur la suite d'épreuves du projet : 274 de ses 474 tests commencent par cette ligne-là.
#
# ET POURTANT IL N'Y A TOUJOURS PAS UNE CLASSE PAR FORME À ÉCRIRE. Ce qui manquait est un *nom*
# lié à un descripteur de type, pas une logique : la fabrique ci-dessous rend une sous-classe
# de la vue générique, et l'unité en déclare une ligne par forme.


_BOUND: dict[tuple, type] = {}


def _bind(view, type_fn, cast):
    """Une vue liée à un type : nommable, constructible, et qui refuse ce qui n'est pas d'elle.

    MÉMOÏSÉE PAR FORME. Deux appels pour le même type rendraient deux classes distinctes, et
    `isinstance` deviendrait faux entre deux valeurs pourtant de la même forme -- y compris
    entre ce qu'une unité déclare et ce qu'une conversion rend. Une forme, une classe.
    """
    cached = _BOUND.get((view, type_fn().representation()))
    if cached is not None:
        return cached

    class Bound(view):
        __slots__ = ()

        @classmethod
        def type(cls):
            return type_fn()

        @classmethod
        def decode(cls, blob, **kwargs):
            """Relire depuis des octets.

            SUR UNE VUE LIÉE SEULEMENT, et c'est dans la nature de l'opération : décoder
            demande de connaître le type avant d'avoir la valeur. Une vue nue le lit dans la
            valeur qu'elle tient déjà — elle n'a rien à décoder.
            """
            return cls(dsviper.Value.decode(blob, type_fn(), _definitions(), **kwargs))

        def __init__(self, value: typing.Any = None):
            value = unwrap(value) if hasattr(value, "_unwrap") else value
            # `isinstance(v, dsviper.Value)` EST TOUJOURS FAUX. La liaison Python déclare une
            # hiérarchie dans son `.pyi` et ne la tient pas à l'exécution : le `__mro__` d'une
            # valeur concrète est `(ValueStructure, object)`. Le contrôle ci-dessous ne se
            # déclenchait donc jamais, et une valeur du mauvais type filait jusqu'au runtime —
            # qui la refusait, mais par une `ViperError` et non par le `TypeError` que le
            # contrat annonce. Reconnaître par une méthode est le seul test qui tienne.
            if hasattr(value, "type_code") and value.type() == type_fn():
                View.__init__(self, value)
                return

            # DEUX FAÇONS DE SE TROMPER, ET UNE SEULE EST UNE ERREUR. `Optional_StructureT(s)`
            # donne l'élément et non le conteneur : c'est la façon la plus courte d'en écrire
            # un, et le runtime sait le bâtir. `Vector_uint8(vector_int8)` donne un conteneur
            # d'un autre type, et là il n'y a rien à bâtir. Laisser le runtime trancher, et
            # traduire son refus dans le `TypeError` que le contrat annonce — par un `raise` et
            # non un `assert`, pour que ça tienne aussi sous `python -O`.
            try:
                View.__init__(self, cast(dsviper.Value.create(type_fn(), unwrap(value))))
            except dsviper.ViperError as refus:
                raise TypeError(
                    f"cette valeur n'est pas un {type_fn().representation()}") from refus

    Bound.__name__ = Bound.__qualname__ = type_fn().representation()
    _BOUND[(view, type_fn().representation())] = Bound
    return Bound


def sequence_of(type_fn):
    return _bind(Sequence, type_fn, lambda v: v)


def mapping_of(type_fn):
    return _bind(Mapping, type_fn, dsviper.ValueMap.cast)


def ordered_of(type_fn):
    return _bind(Ordered, type_fn, dsviper.ValueXArray.cast)


def optional_of(type_fn):
    return _bind(Optional, type_fn, dsviper.ValueOptional.cast)


def variant_of(type_fn):
    return _bind(Variant, type_fn, dsviper.ValueVariant.cast)


def _alternative_name(type_) -> str:
    """Le nom d'une alternative, tel qu'un appelant l'écrit.

    `Demo::StructureS` s'écrit `Demo_StructureS`, `string` s'écrit `string` : c'est la
    représentation du type, dont le séparateur de portée devient un souligné — le seul
    caractère qu'un identifiant accepte.
    """
    return type_.representation().replace("::", "_")


def _forward(view: View, name: str) -> typing.Any:
    """Transmettre à la valeur ce que la vue ne nomme pas, en enveloppant ce qui revient."""
    inner: typing.Any = getattr(view.vpr_value, name, None)
    if inner is None:
        raise AttributeError(f"ni la vue ni {view.vpr_value.type().representation()} n'ont '{name}'")
    if not callable(inner):
        return wrap(inner)

    def forwarded(*args, **kwargs) -> typing.Any:
        result: typing.Any = inner(*[unwrap(a) for a in args], **kwargs)
        if hasattr(result, "type_code"):
            return type(view)(result) if result.type() == view.vpr_value.type() else wrap(result)
        if isinstance(result, tuple):
            return tuple(wrap(r) if hasattr(r, "type_code") else r for r in result)
        return result

    return forwarded
