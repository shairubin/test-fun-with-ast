import ast


def simple_example():
    print("Shai Hello World!")
    x= ast.parse('x += 5')
    x_dump= ast.dump(x, include_attributes=False, indent=5)
    print(x_dump)

if __name__ == "__main__":
    simple_example()