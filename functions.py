from ProjetoLogicaComp.formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):


    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)



def atoms(formula):

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = atoms(formula.left)
        sub2 = atoms(formula.right)
        return sub1.union(sub2)


def number_of_atoms(formula):

    if isinstance(formula, Atom):
        return 1

    if isinstance(formula, Not):
       return number_of_atoms(formula.inner)

    if isinstance(formula, Not) or isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)

def number_of_connectives(formula):

    if isinstance(formula, Atom):
        return 0

    if isinstance(formula, Not):
       return number_of_connectives(formula.inner) + 1

    if isinstance(formula, Not) or isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1

def substitution(formula, old_subformula, new_subformula):

    if isinstance(formula, Atom) and (formula != old_subformula):
        return formula

    elif formula == old_subformula:
        return new_subformula

    elif isinstance(formula, Not) and (formula != old_subformula) :
        return Not(substitution(formula.inner, old_subformula, new_subformula))

    elif isinstance(formula, Implies) and (formula != old_subformula):
        return Implies(substitution(formula.left,old_subformula,new_subformula),
                       substitution(formula.right,old_subformula,new_subformula))

    elif isinstance(formula, And) and (formula != old_subformula):
        return And(substitution(formula.left, old_subformula, new_subformula),
                   substitution(formula.right, old_subformula, new_subformula))

    elif isinstance(formula, Or) and (formula != old_subformula):
        return Or(substitution(formula.left, old_subformula, new_subformula),
                  substitution(formula.right, old_subformula, new_subformula))

