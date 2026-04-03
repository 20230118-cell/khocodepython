import ast

def get_ast_nodes(code):
    try:
        tree = ast.parse(code)
        nodes = [type(node).__name__ for node in ast.walk(tree)]
        return nodes
    except Exception as e:
        print("❌ Lỗi AST:", e)
        return None   # ⚠️ QUAN TRỌNG: không dùng []


def compare_ast(code1, code2):
    nodes1 = get_ast_nodes(code1)
    nodes2 = get_ast_nodes(code2)

    # ❗ Nếu parse lỗi
    if nodes1 is None or nodes2 is None:
        print("⚠️ Không phân tích được AST")
        return 0

    if not nodes1 or not nodes2:
        return 0

    set1 = set(nodes1)
    set2 = set(nodes2)

    common = set1.intersection(set2)

    similarity = len(common) / max(len(set1), len(set2)) * 100

    return similarity