from Create_Username import CreateUsername
from Create_Graph import CreateGraph
from Create_Post_Value import CreatePostValue


def main():
    username = CreateUsername()
    username.create_username()

    user_graph = CreateGraph()
    user_graph.create_graph()

    post_value = CreatePostValue()
    post_value.create_value()

if __name__ == "__main__":
    main()

