from sympy import Eq, symbols, solve, sympify, Rational

def verify_solution_steps_sympy(equations, steps, final_solution):
    
    x,y=symbols("x y")
    
    try:
        eqs=[]
        for eq in equations:
            lhs,rhs=eq.split("=")
            eqs.append(Eq(sympify(lhs), sympify(rhs)))
            
        correct_ans=solve(eqs,(x,y))
        
        if correct_ans != final_solution:
            print(f"Incorrect final solution. Expected: {correct_ans}, but got: {final_solution}.")
        else:
            print("Answer is correct lets check for steps")

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
steps = [
    "Step 1: y = (5 - 2*x)/3",
    "Step 2: Substituting into 4*x - y = 7",
    "Step 3: 4*x - (5 - 2*x)/3 = 7",
    "Step 4: Solve for x, x = 13/7",
    "Step 5: Solve for y, y = 3/7"
]

final_solution = {symbols("x"): Rational(13, 7), symbols("y"): Rational(3,7)}  # Correct answer

result = verify_solution_steps_sympy(equations, steps, final_solution)
print(result)