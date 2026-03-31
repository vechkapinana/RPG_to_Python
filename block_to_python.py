def block_to_python(block):
    content = block["content"]
    if content["type"] == "if":
        cond = content["condition"]
        left = cond["left"]
        op = cond["op"]
        right = cond["right"]
        
        py_lines = []
        py_lines.append(f"if {left} {op} {right}:")
        for stmt in content.get("then", []):
            py_lines.append(f"    {stmt['target']} = {stmt['value']}")
        if content.get("else"):
            py_lines.append("else:")
            for stmt in content["else"]:
                py_lines.append(f"    {stmt['target']} = {stmt['value']}")
        return "\n".join(py_lines)
    return ""