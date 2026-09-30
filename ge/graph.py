from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph


def create(attachment_mutating: AttachmentMutating, name: str) -> graph.GraphKey:
    graph_key = graph.GraphKey.create()

    description = graph.GraphDescription()
    description.name = name

    attachments.Graph.description.set(attachment_mutating, graph_key, description)
    attachments.Graph.topology.set(attachment_mutating, graph_key, graph.GraphTopology())
    attachments.Graph.tags.set(attachment_mutating, graph_key, containers.Map_of_string_to_string())
    attachments.Graph.comments.set(attachment_mutating, graph_key, containers.XArray_of_string())
    attachments.Graph.selection.set(attachment_mutating, graph_key, graph.GraphSelection())

    return graph_key
