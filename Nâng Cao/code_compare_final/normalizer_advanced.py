import ast

class RenameVariables(ast.NodeTransformer):
    def __init__(self):
        self.var_map = {}
        self.counter = 0

    def new_name(self):
        self.counter += 1
        return f"var{self.counter}"

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Load)):
            if node.id not in self.var_map:
                self.var_map[node.id] = self.new_name()
            node.id = self.var_map[node.id]
        return node


def normalize_code_advanced(code):
    try:
        tree = ast.parse(code)

        transformer = RenameVariables()
        tree = transformer.visit(tree)

        ast.fix_missing_locations(tree)

        normalized = ast.unparse(tree)

        # bỏ khoảng trắng nâng cao
        normalized = "\n".join(
            line.strip() for line in normalized.split("\n") if line.strip()
        )

        return normalized

    except Exception as e:
        print("Lỗi chuẩn hóa:", e)
        return code