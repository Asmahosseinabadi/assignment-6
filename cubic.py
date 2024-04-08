import cmath 
import math

def solve_cubic(a, b, c, d):
    
    delta = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    
    delta_cubed_root = cmath.sqrt(delta)
    
    term1 = -b**2 / (3*a**2) + delta_cubed_root / (3*a**2)
    
    term2 = -b**2 / (3*a**2) - delta_cubed_root / (3*a**2)
    
    cubic_root_term1 = cmath.sqrt(term1)
    
    cubic_root_term2 = cmath.sqrt(term2)
    
    root1 = cubic_root_term1 + cubic_root_term2
    
    root2 = -cubic_root_term1 + cubic_root_term2
    
    root3 = -b / (3*a) + (term1 + term2) / (3*a)
    
    return root1, root2, root3

# Example usage
a = int(input("enter the a:"))
b = int(input("enter the b:"))
c = int(input("enter the c:"))
d = int(input("enter the d:"))

root1, root2, root3 = solve_cubic(a, b, c, d)
print(f"The roots of the cubic equation are: {root1}, {root2}, {root3}")
