from Create_Username import CreateUsername
from Create_Graph import CreateGraph


def main():
    username = CreateUsername()
    username.create_username()

    user_graph = CreateGraph()
    user_graph.create_graph()



if __name__ == "__main__":
    main()

