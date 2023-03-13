""" Handy utilities for woot. """
import re
import functools
import inspect


def extract_path_params(path_string):
    return re.findall(r"\{([^}]*)\}", path_string)


def get_account_name(class_name: str) -> str:
    """Get account name from class name."""
    return split_by_uppercase(
        class_name.replace("Resource", "").replace("Async", "")
    ).lower()


def split_by_uppercase(input_str):
    parts = re.findall("[A-Z][^A-Z]*", input_str)
    return "_".join(parts)


def update_signature(fields, name, params):
    def decorator(func):
        signs = [
            inspect.Parameter("self", inspect.Parameter.POSITIONAL_ONLY),
        ]

        path_docs = []
        for k in params:
            x = inspect.Parameter(k, inspect.Parameter.POSITIONAL_OR_KEYWORD)
            x = x.replace(annotation=str)
            signs.append(x)
            path_docs.append(f"{k}: str")

        field_docs = []
        for k, v in fields.items():
            x = inspect.Parameter(k, inspect.Parameter.POSITIONAL_OR_KEYWORD)
            x = x.replace(annotation=v.type)
            signs.append(x)
            field_docs.append(f"{k}: {v.type}")
        func.__signature__ = inspect.Signature(signs)
        # Create a docstring that describes the fields
        p_string = "\n".join(path_docs)
        f_string = "\n".join(field_docs)
        docstring = (
            f"{name}({', '.join(params + list(fields.keys()))})\n\n"
            f"Path parameters:\n"
            f"{'-' * 20}\n"
            f"{p_string}"
            f"\n"
            f"Body schema:\n"
            f"{'-' * 20}\n"
            f"{f_string}"
            f"\n\n"
        )
        # Set the new docstring
        func.__doc__ = docstring

        return func

    return decorator
