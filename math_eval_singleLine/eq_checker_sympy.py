from sympy import Eq, simplify,SympifyError, sympify

def check_equivalence_with_sympy(expr1, expr2):
    try:
        lhs1,rhs1=expr1.split('=')
        lhs2,rhs2=expr2.split('=')
        
        #make sympy expression
        lhs1_expr = sympify(lhs1.strip())
        rhs1_expr = sympify(rhs1.strip())
        lhs2_expr = sympify(lhs2.strip())
        rhs2_expr = sympify(rhs2.strip())
        
        eq1=Eq(lhs1_expr,rhs1_expr)
        eq2=Eq(lhs2_expr,rhs2_expr)
        
        difference = simplify(eq1.lhs - eq2.lhs) - simplify(eq1.rhs - eq2.rhs)        

        if difference == 0:
            print("The expressions are equivalent.")
            return True
        else:
            print("The expressions are not equivalent.")
            return False
    except SympifyError:
        print("One or both expressions are invalid.")
        return False

# Example usage
expression1 = "2*x + 3*x = 5 "
expression2 = "0 = 5*x - 5 "
check_equivalence_with_sympy(expression1, expression2)

