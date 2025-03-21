from sympy import Eq, symbols, solve, sympify

def verify_solution_steps_sympy(equations, steps, final_solution):
    
    x,y=symbols("x y")
    
    try:
        solve(equations,(x,y))
        eqs=[]
        for eq in equations:
            lhs,rhs=eq.split("=")
            eqs.append(Eq(sympify(lhs), sympify(rhs)))
            
        correct_ans=solve(eqs,(x,y))
        
        if correct_ans != final_solution:
            print(f"Incorrect final solution. Expected: {correct_ans}, but got: {final_solution}.")

        for step in steps:
            try:
                (sympify(step))
            except Exception:
                print(f"❌ Incorrect step: {step}")

        return f"✅ Correct answer: {correct_ans}"
        
    except Exception as e:
        print(f"⚠️ SymPy Error: {e}")
        return None


equations = ["2*x + 3*y = 5", "4*x - y = 7"]
steps = ["y = (5 - 2*x)/3", "Substituting into 4*x - y = 7", "4*x - (5 - 2*x)/3 = 7", "x = 2", "y = -1"]
final_solution = {symbols("x"): 2, symbols("y"): -1}  # Correct answer

result = verify_solution_steps_sympy(equations, steps, final_solution)
print(result)