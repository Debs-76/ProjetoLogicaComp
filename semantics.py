from ProjetoLogicaComp.formula import *
from ProjetoLogicaComp.functions import atoms
from functools import reduce

def truth_value(formula, interpretation):
    if isinstance(formula, Atom):
        for i in interpretation:
            if formula.__eq__(i):
                return interpretation[i]
        return None

    if isinstance(formula, Not):
        return None if truth_value(formula.inner, interpretation) is None else (
            not truth_value(formula.inner, interpretation))


    if isinstance(formula, Implies):
        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return None if left is None else False if left is True and right is False else True

    if isinstance(formula, And):
        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return None if (left is None or right is None) else True if (left and right) else False

    if isinstance(formula, Or):
        left = truth_value(formula.left, interpretation)

        right = truth_value(formula.right, interpretation)

        return True if left or right else None if left is None or right is None else False



def is_logical_consequence(premises, conclusion):
    and_premises = reduce(lambda x, y: And(x, y), premises)
    if is_satisfiable(And(and_premises, Not(conclusion))):
        return False
    return True




def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========




def is_valid(formula):


    return True if is_satisfiable(Not(formula)) is False else False




def is_satisfiable(formula):


    atoms_list = atoms(formula)
    partial_interpretation = get_partial_interpretation(formula)

    if partial_interpretation:
        atoms_list = remove_atoms(atoms_list.copy(), partial_interpretation)
        return sat(formula, atoms_list, partial_interpretation)

    else:
        return sat(formula, atoms_list, {})




def sat(formula, atoms_list, interpretation):
    if len(atoms_list) == 0:
        result = truth_value(formula, interpretation)

        return interpretation if result else False

    atom = atoms_list.pop()

    interpretation1 = union_dict(interpretation, {atom: True})
    interpretation2 = union_dict(interpretation, {atom: False})

    result = sat(formula, atoms_list.copy(), interpretation1)

    if result:
        return result

    return sat(formula, atoms_list.copy(), interpretation2)


def get_partial_interpretation(formula):
    if isinstance(formula, Atom):
        return {formula: True}

    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return {formula.inner: False}

    if isinstance(formula, And):

        left = get_partial_interpretation(formula.left)
        right = get_partial_interpretation(formula.right)

        if (left and right):
            return union_dict(left, right)

        return None


def remove_atoms(formula, interpretation):
    atoms_list = []
    for atom in atoms_list:
        if atom not in interpretation:
            atoms_list.append(atom)
    return atoms_list


def union_dict(inter1: dict, inter2: dict):
    return {**inter1, **inter2}