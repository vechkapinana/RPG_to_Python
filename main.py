from parser import parse_rpg
from semantic import to_semantic
from anchors import add_anchors
from block_to_python import block_to_python
from grace_pipeline import GracePipeline
from agent import LLMAgent

code = [
    "C* Сравнение возраста",
    "C     AGE           IFGE      18",
    "C                   MOVE      'YES'         ALLOWED",
    "C                   ELSE",
    "C                   MOVE      'NO'          ALLOWED",
    "C                   ENDIF"
]

parsed = parse_rpg(code)
print(parsed)
semantic = to_semantic(parsed)
print(semantic)
anchored = add_anchors(semantic)
print(anchored)
for block in anchored:
    py_code = block_to_python(block)
    print(py_code)

pipeline = GracePipeline()
result = pipeline.run(anchored)

for r in result:
    print(r)