# 1.Examine the nested functions in the code editor. Let’s try to examine the enclosing namespace.
# At the line that says # Add locals() call below: print the locals() function.
# Spot anything significant?

global_variable = 'global'


def outer_function():
    outer_value = "outer"

    def inner_functon():
        inner_value = "inner"

        def inner_nested_function():
            nested_value = 'nested'
        inner_nested_function()
        # Add locals() below
        print(locals())
    inner_functon()


outer_function()
