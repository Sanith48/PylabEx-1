import math

def calculate_area(a, b, c):
    """Calculate the area of a triangle using Heron's formula."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    # Input sides for the first triangle
    print("Enter the sides of the first triangle:")
    a1 = float(input("Side a: "))
    b1 = float(input("Side b: "))
    c1 = float(input("Side c: "))
    
    # Input sides for the second triangle
    print("\nEnter the sides of the second triangle:")
    a2 = float(input("Side a: "))
    b2 = float(input("Side b: "))
    c2 = float(input("Side c: "))
    
    # Calculate areas of both triangles
    area1 = calculate_area(a1, b1, c1)
    area2 = calculate_area(a2, b2, c2)
    
    # Total area
    total_area = area1 + area2
    
    # Calculate contributions
    contribution1 = (area1 / total_area) * 100
    contribution2 = (area2 / total_area) * 100
    
    # Print results
    print(f"\nArea of the first triangle: {area1:.2f}")
    print(f"Area of the second triangle: {area2:.2f}")
    print(f"Total area: {total_area:.2f}")
    print(f"Contribution of the first triangle: {contribution1:.2f}%")
    print(f"Contribution of the second triangle: {contribution2:.2f}%")

if __name__ == "__main__":
    main()

