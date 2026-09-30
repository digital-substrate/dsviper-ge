"""Ce dont le code généré a besoin, et que le modèle ne décide pas.

CE PAQUET NE NOMME AUCUN TYPE D'AUCUN MODÈLE. C'est sa définition : tout ce qui est ici est
identique pour tout modèle, donc rien n'a à être produit par un générateur. Ce qui varie --
les concepts, les structures, les attachments -- est généré ; ce qui ne varie pas est ici,
écrit une fois.

La mesure qui l'a décidé : le pack de templates Python fait 2 200 lignes et en rend 12 338
pour un modèle moyen, dont environ 700 lignes de template produisent une classe par forme de
conteneur rencontrée -- `Optional_Colour`, `Vector_Parts_Colour`. Or `Optional_Colour` et
`Optional_int32` ne diffèrent que par le descripteur du type et la classe qui enveloppe un
élément, et la valeur porte déjà les deux.

SA PLACE EST DANS LA LIAISON, ET IL N'Y EST PAS. Le code rendu l'importe donc depuis le
paquet lui-même, où `render-python.py` le dépose :

    from .._codegen import AttachmentProxy, Mapping, Ordered, Proxy, Sequence
    from .._codegen import register, unwrap, wrap

Le jour où `dsviper` le portera, ce sera `from dsviper.codegen import …` : une ligne dans
chacun des trois templates, et rien d'autre. Un sous-paquet et non la racine, parce que
`wrap`, `unwrap` et `register` sont des mots trop généraux pour le premier niveau d'un
paquet qui en expose déjà deux cents -- et parce que `Attachment` y est déjà pris par le
descripteur, ce qui est aussi pourquoi l'accesseur typé s'appelle `AttachmentProxy`.
"""

from .attachment import AttachmentProxy
from .container import (Mapping, Optional, Ordered, Sequence, Variant, View,
                        mapping_of, optional_of, ordered_of, sequence_of, variant_of)
from .proxy import (NEUF, AnyConceptKey, Proxy, is_known, register,
                    set_definitions, unwrap, wrap)

__all__ = [
    "NEUF",
    "AnyConceptKey",
    "AttachmentProxy",
    "Mapping",
    "Ordered",
    "Proxy",
    "is_known",
    "Optional",
    "Sequence",
    "Variant",
    "View",
    "mapping_of",
    "optional_of",
    "ordered_of",
    "sequence_of",
    "variant_of",
    "register",
    "set_definitions",
    "unwrap",
    "wrap",
]
