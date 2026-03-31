import uuid

def add_anchors(semantic):
    anchored = []

    for block in semantic:
        anchor = {
            "anchor_id": str(uuid.uuid4()),
            "anchor_type": block["type"],
            "content": block
        }

        anchored.append(anchor)

    return anchored