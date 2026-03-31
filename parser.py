def smart_parse_fixed(line):
    for op in ["IFGE", "MOVE", "ELSE", "ENDIF"]:
        if op in line:
            parts = line.split(op)

            left = parts[0].replace("C", "").strip()
            right = parts[1].strip() if len(parts) > 1 else ""

            return {
                "factor1": left,
                "opcode": op,
                "factor2": right.split()[0] if right else "",
                "result": right.split()[1] if len(right.split()) > 1 else ""
            }
    
def parse_rpg(lines):
    parsed = []

    for line in lines:
        line = line.rstrip()

        if not line or line.startswith("C*"):
            continue

        record = smart_parse_fixed(line)
        opcode = record["opcode"]

        # ищем ключевые операции
        if opcode == "IFGE":
            record["args"] = [record["factor1"], record["factor2"]]

        elif opcode == "MOVE":
            record["args"] = [record["factor2"], record["result"]]

        elif opcode in ["ELSE", "ENDIF"]:
            record["args"] = []


        parsed.append(record)

    return parsed

