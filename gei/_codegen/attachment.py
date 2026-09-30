"""L'accesseur typé d'un attachment : ce qui est commun à tous, écrit une fois.

CE FICHIER NE NOMME AUCUN TYPE DU MODÈLE. Ce qui ne dépend que de l'identité d'un
attachment — lire, écrire, énumérer, comparer le document entier — ne fait que passer le
descripteur à `AttachmentGetting` ou `AttachmentMutating`, et vit ici une fois.

CE QUI DÉPEND DU DOCUMENT EST GÉNÉRÉ, ET C'EST VOULU. `union_vertex_keys`, `set_color` : ce
sont les opérations avec lesquelles s'écrivent les fonctions métier, et elles doivent se
compléter, se typer et échouer à l'import plutôt qu'à l'appel. Une unité en déclare donc une
classe par attachment, dont chaque méthode appelle l'une des primitives protégées d'ici.
"""

from __future__ import annotations

import functools
import typing
from typing import Callable

import dsviper

from .proxy import unwrap as _unwrap, wrap as _wrap


K = typing.TypeVar("K")
D = typing.TypeVar("D")


class AttachmentProxy(typing.Generic[K, D]):
    """Un attachment du modèle, vu depuis l'unité qui le déclare.

    `AttachmentProxy` ET NON `Attachment`, PARCE QUE `dsviper.Attachment` EXISTE ET N'EST PAS
    ÇA. Le sien est le *descripteur* -- ce que les définitions portent : un identifiant, un
    type de clé, un type de document. Celui-ci est l'accesseur typé qui le résout et s'en
    sert, comme `Proxy` est l'accesseur typé d'une `Value`. Tant que les deux vivent dans
    des modules différents la confusion n'est que de lecture ; le jour où ceux-ci entrent
    dans `dsviper`, où ils ont vocation à aller, deux `Attachment` dans un même module
    s'écrasent -- et c'est le dernier des deux qui gagne, sans un mot.

    LA BASE N'A PRESQUE PAS DE MÉTHODES À ELLE. `dsviper.Database` n'hérite pas
    d'`AttachmentGetting` — la liaison Python ne les relie pas — mais elle porte les mêmes
    `keys`, `has`, `get` et `set`, et rien ici ne demande davantage : chaque méthode ne fait
    que passer le descripteur. Il ne reste en propre que `delete`, qu'un état en mémoire
    n'offre pas. C'est le même constat qu'en C++, où cinq gabarits étaient devenus deux.
    """

    # Pas de __slots__ : `cached_property` écrit son résultat dans l'instance.

    def __init__(self, runtime_id: dsviper.ValueUUId,
                 definitions: Callable[[], dsviper.DefinitionsConst],
                 key: type, document: type | None):
        self._runtime_id = runtime_id
        self._definitions = definitions

        # LES DEUX CLASSES NE SERVENT PAS À CONVERTIR — `wrap` le fait depuis le type que la
        # valeur porte. Elles sont retenues parce que les nommer dans l'unité **force leur
        # import**, et que c'est l'import qui remplit la table des classes. Sans elles la
        # conversion marcherait tant que quelqu'un d'autre a importé l'unité d'abord, ce qui
        # est la pire forme de correction : celle qui dépend de l'ordre.
        self._key = key
        self._document = document

    @functools.cached_property
    def descriptor(self) -> dsviper.Attachment:
        """Le descripteur que le runtime en tire, résolu une fois.

        PUBLIC PARCE QUE TOUT LE MONDE LE DEMANDE : les cinq opérations, l'épreuve sur base,
        le pont dynamique. Une identité, un endroit.
        """
        return self._definitions().check_attachment(self._runtime_id)

    # ── lire ──
    #
    # Le contexte est le premier paramètre, et il est le seul que l'appelant ne pourrait pas
    # deviner : c'est lui qui dit sur quoi l'appel porte — un état en mémoire, une base.

    def keys(self, getting: dsviper.AttachmentGetting) -> set[K]:
        return {_wrap(key) for key in getting.keys(self.descriptor)}

    def has(self, getting: dsviper.AttachmentGetting, key: K) -> bool:
        return getting.has(self.descriptor, key.vpr_value)

    def get(self, getting: dsviper.AttachmentGetting, key: K) -> D | None:
        """Le document, ou `None` — et non un `Optional` enveloppé.

        LE PACK REND UN `Optional_Colour`, UN PROXY DE PLUS À NOMMER ET À GÉNÉRER. Python a
        déjà `None` et `if x is None`, qui disent la même chose sans qu'une classe existe
        pour ça. C'est l'écart le plus visible avec la sortie du pack, et il est délibéré.
        """
        document = getting.get(self.descriptor, key.vpr_value)
        return None if document.is_nil() else _wrap(document.unwrap())

    def enumerate(self, getting, *, encoded: bool = True) -> list[tuple[K, D]]:
        """Les paires clé/document, telles que le runtime les rend."""
        # UNE BASE N'ÉNUMÈRE PAS ELLE-MÊME : elle offre l'interface de lecture qui le fait.
        source = getting if hasattr(getting, "enumerate") else getting.attachment_getting()
        return [(_wrap(key), _wrap(document) if isinstance(document, dsviper.Value) else document)
                for key, document in source.enumerate(self.descriptor, encoded=encoded)]

    def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                  ) -> tuple[set[K], set[K], set[K], set[K]]:
        added, removed, different, same = dsviper.AttachmentGetting.diff_keys(
            current, other, self.descriptor)
        return tuple({_wrap(key) for key in group}
                     for group in (added, removed, different, same))

    # ── écrire ──

    def set(self, mutating: dsviper.AttachmentMutating | dsviper.Database, key: K, value: D):
        """Poser le document.

        Rend ce que le contexte rend : rien pour un état en mémoire, un statut pour une
        base — un enregistrement peut échouer là où un changement en mémoire ne le peut pas.
        """
        return mutating.set(self.descriptor, key.vpr_value, _unwrap(value))

    def delete(self, database: dsviper.Database, key: K) -> bool:
        """Retirer le document. La seule opération qu'une base ajoute."""
        return database.delete(self.descriptor, key.vpr_value)

    def diff(self, mutating: dsviper.AttachmentMutating, key: K, value: D, *, recursive: bool = False) -> None:
        mutating.diff(self.descriptor, key.vpr_value, _unwrap(value), recursive=recursive)

    # ── les primitives des méthodes générées ──
    #
    # UNE PAR OPÉRATION DU RUNTIME, ET AUCUNE N'EST PUBLIQUE. Le champ est nommé comme le
    # modèle le déclare, parce que c'est le nom du chemin ; `None` désigne la racine, pour un
    # document qui est lui-même un set, une map ou une xarray. Une unité les appelle depuis
    # des méthodes qui portent le nom et les types de chaque champ — c'est là que l'appelant
    # trouve la complétion, pas ici.

    def _update(self, mutating: dsviper.AttachmentMutating, key, field: str, value) -> None:
        mutating.update(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _union_in_set(self, mutating: dsviper.AttachmentMutating, key, field: str | None, value) -> None:
        mutating.union_in_set(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _subtract_in_set(self, mutating: dsviper.AttachmentMutating, key, field: str | None, value) -> None:
        mutating.subtract_in_set(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _union_in_map(self, mutating: dsviper.AttachmentMutating, key, field: str | None, value) -> None:
        mutating.union_in_map(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _subtract_in_map(self, mutating: dsviper.AttachmentMutating, key, field: str | None, value) -> None:
        mutating.subtract_in_map(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _update_in_map(self, mutating: dsviper.AttachmentMutating, key, field: str | None, value) -> None:
        mutating.update_in_map(self.descriptor, key.vpr_value, _path(field), _unwrap(value))

    def _insert_in_xarray(self, mutating: dsviper.AttachmentMutating, key, field: str | None,
                          before_position: dsviper.ValueUUId, new_position: dsviper.ValueUUId,
                          value) -> None:
        mutating.insert_in_xarray(self.descriptor, key.vpr_value, _path(field),
                                  before_position, new_position, _unwrap(value))

    def _update_in_xarray(self, mutating: dsviper.AttachmentMutating, key, field: str | None,
                          position: dsviper.ValueUUId, value) -> None:
        mutating.update_in_xarray(self.descriptor, key.vpr_value, _path(field), position, _unwrap(value))

    def _remove_in_xarray(self, mutating: dsviper.AttachmentMutating, key, field: str | None,
                          position: dsviper.ValueUUId) -> None:
        mutating.remove_in_xarray(self.descriptor, key.vpr_value, _path(field), position)

    def __repr__(self) -> str:
        return f"AttachmentProxy({self.descriptor.representation()})"


@functools.cache
def _path(field: str | None) -> dsviper.PathConst:
    """Le chemin d'un champ, ou la racine ; construit une fois par nom."""
    return (dsviper.Path() if field is None else dsviper.Path.from_field(field)).const()
