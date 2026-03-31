def to_semantic(parsed):
    semantic = []
    stack = []

    for item in parsed:
        if item["opcode"] == "IFGE":
            condition = {
                "type": "if",
                "condition": {
                    "left": item["args"][0],
                    "op": ">=",
                    "right": item["args"][1]
                },
                "then": [],
                "else": []
            }
            stack.append(condition)

        elif item["opcode"] == "MOVE":
            operation = {
                "type": "assign",
                "value": item["args"][0],
                "target": item["args"][1]
            }

            if stack:
                if "else_mode" in stack[-1]:
                    stack[-1]["else"].append(operation)
                else:
                    stack[-1]["then"].append(operation)

        elif item["opcode"] == "ELSE":
            stack[-1]["else_mode"] = True

        elif item["opcode"] == "ENDIF":
            finished = stack.pop()
            semantic.append(finished)

    return semantic