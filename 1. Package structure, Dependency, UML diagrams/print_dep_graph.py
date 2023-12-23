import pydeps


def generate_class_dependency_graph(package_path, output_path):
    pydeps_args = [package_path, "-o", output_path]
    pydeps.run(pydeps_args)


# Example usage
package_path = r"C:\Users\kinla\Documents\All_github_repo\gites\gites"
output_path = r"C:\Users\kinla\Documents\All_github_repo\gites\graph"
generate_class_dependency_graph(package_path, output_path)