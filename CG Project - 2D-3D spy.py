import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

# Function to plot 2D shapes

def plot_shape_2d(original, transformed, operation):
    original = np.vstack((original, original[0]))  # Close the polygon
    transformed = np.vstack((transformed, transformed[0]))
    
    plt.figure()
    plt.plot(original[:, 0], original[:, 1], 'bo-', label='Original Shape')
    plt.plot(transformed[:, 0], transformed[:, 1], 'ro-', label=f'Transformed Shape ({operation})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{operation} Operation in 2D')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot 3D shapes
def plot_shape_3d(original, transformed, operation):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    original = np.vstack((original, original[0]))  # Close the polygon
    transformed = np.vstack((transformed, transformed[0]))

    ax.plot(original[:, 0], original[:, 1], original[:, 2], 'bo-', label='Original Shape')
    ax.plot(transformed[:, 0], transformed[:, 1], transformed[:, 2], 'ro-', label=f'Transformed Shape ({operation})')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'{operation} Operation in 3D')
    plt.legend()
    plt.show()

# Functions for 2D transformations
def translate_2d(shape, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(translation_matrix.T)
    return transformed_shape[:, :2]

def scale_2d(shape, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(scaling_matrix.T)
    return transformed_shape[:, :2]

def rotate_2d(shape, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0],
                                [np.sin(rad), np.cos(rad), 0],
                                [0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(rotation_matrix.T)
    return transformed_shape[:, :2]

def reflect_2d(shape, axis):
    if axis == 'x':
        reflection_matrix = np.array([[1, 0, 0],
                                      [0, -1, 0],
                                      [0, 0, 1]])
    elif axis == 'y':
        reflection_matrix = np.array([[-1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(reflection_matrix.T)
    return transformed_shape[:, :2]

# Function for 2D shearing
def shear(shape, shx, shy):
    shearing_matrix = np.array([[1, shx, 0],
                                [shy, 1, 0],
                                [0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(shearing_matrix.T)
    return transformed_shape[:, :2]

# Functions for 3D transformations (already defined previously)
def translate_3d(shape, tx, ty, tz):
    translation_matrix = np.array([[1, 0, 0, tx],
                                   [0, 1, 0, ty],
                                   [0, 0, 1, tz],
                                   [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(translation_matrix.T)
    return transformed_shape[:, :3]

def scale_3d(shape, sx, sy, sz):
    scaling_matrix = np.array([[sx, 0, 0, 0],
                               [0, sy, 0, 0],
                               [0, 0, sz, 0],
                               [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(scaling_matrix.T)
    return transformed_shape[:, :3]

def rotate_x_3d(shape, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[1, 0, 0, 0],
                                [0, np.cos(rad), -np.sin(rad), 0],
                                [0, np.sin(rad), np.cos(rad), 0],
                                [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(rotation_matrix.T)
    return transformed_shape[:, :3]

def rotate_y_3d(shape, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), 0, np.sin(rad), 0],
                                [0, 1, 0, 0],
                                [-np.sin(rad), 0, np.cos(rad), 0],
                                [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(rotation_matrix.T)
    return transformed_shape[:, :3]

def rotate_z_3d(shape, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0, 0],
                                [np.sin(rad), np.cos(rad), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(rotation_matrix.T)
    return transformed_shape[:, :3]

def reflect_3d(shape, plane):
    if plane == 'xy':
        reflection_matrix = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, -1, 0],
                                      [0, 0, 0, 1]])
    elif plane == 'yz':
        reflection_matrix = np.array([[-1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])
    elif plane == 'xz':
        reflection_matrix = np.array([[1, 0, 0, 0],
                                      [0, -1, 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])
    shape_homogeneous = np.hstack((shape, np.ones((shape.shape[0], 1))))
    transformed_shape = shape_homogeneous.dot(reflection_matrix.T)
    return transformed_shape[:, :3]

# Main function to take user input and perform the operation
def main():
    print("Choose 2D or 3D Transformations:")
    print("1. 2D Transformation")
    print("2. 3D Transformation")
    dimension = int(input("Enter your choice (1 or 2): "))

    if dimension == 1:  # 2D Transformation
        print("Enter the coordinates of the 2D shape (at least 3 points for a polygon):")
        n = int(input("Enter the number of points: "))
        shape = []
        for i in range(n):
            x, y = map(float, input(f"Enter x and y coordinates of point {i+1}: ").split())
            shape.append([x, y])
        
        shape = np.array(shape)
        
        print("\nSelect the 2D operation to perform:")
        print("1. Translation")
        print("2. Scaling")
        print("3. Rotation")
        print("4. Reflection")
        print("5. Shearing")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            tx = float(input("Enter translation along X (tx): "))
            ty = float(input("Enter translation along Y (ty): "))
            transformed_shape = translate_2d(shape, tx, ty)
            plot_shape_2d(shape, transformed_shape, "Translation")
        
        elif choice == 2:
            sx = float(input("Enter scaling factor along X (sx): "))
            sy = float(input("Enter scaling factor along Y (sy): "))
            transformed_shape = scale_2d(shape, sx, sy)
            plot_shape_2d(shape, transformed_shape, "Scaling")
        
        elif choice == 3:
            angle = float(input("Enter rotation angle (in degrees): "))
            transformed_shape = rotate_2d(shape, angle)
            plot_shape_2d(shape, transformed_shape, "Rotation")
        
        elif choice == 4:
            axis = input("Enter reflection axis (x or y): ")
            transformed_shape = reflect_2d(shape, axis)
            plot_shape_2d(shape, transformed_shape, "Reflection")
            
        elif choice == 5:
            shx = float(input("Enter shearing factor along X (shx): "))
            shy = float(input("Enter shearing factor along Y (shy): "))
            transformed_shape = shear(shape, shx, shy)
            plot_shape_2d(shape, transformed_shape, "Shearing")
        
        else:
            print("Invalid choice! Please choose between 1 and 5.")
    
    elif dimension == 2:  # 3D Transformation
        n = int(input("Enter the number of points: "))
        shape = []
        for i in range(n):
            x, y, z = map(float, input(f"Enter x, y, and z coordinates of point {i+1}: ").split())
            shape.append([x, y, z])
        
        shape = np.array(shape)

        print("\nSelect the 3D operation to perform:")
        print("1. Translation")
        print("2. Scaling")
        print("3. Rotation")
        print("4. Reflection")

        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            tx = float(input("Enter translation along X (tx): "))
            ty = float(input("Enter translation along Y (ty): "))
            tz = float(input("Enter translation along Z (tz): "))
            transformed_shape = translate_3d(shape, tx, ty, tz)
            plot_shape_3d(shape, transformed_shape, "Translation")
        
        elif choice == 2:
            sx = float(input("Enter scaling factor along X (sx): "))
            sy = float(input("Enter scaling factor along Y (sy): "))
            sz = float(input("Enter scaling factor along Z (sz): "))
            transformed_shape = scale_3d(shape, sx, sy, sz)
            plot_shape_3d(shape, transformed_shape, "Scaling")
        
        elif choice == 3:
            axis = input("Enter the axis of rotation (x, y, or z): ").lower()
            angle = float(input("Enter rotation angle (in degrees): "))
            if axis == 'x':
                transformed_shape = rotate_x_3d(shape, angle)
            elif axis == 'y':
                transformed_shape = rotate_y_3d(shape, angle)
            elif axis == 'z':
                transformed_shape = rotate_z_3d(shape, angle)
            else:
                print("Invalid axis!")
                return
            plot_shape_3d(shape, transformed_shape, "Rotation")
        
        elif choice == 4:
            plane = input("Enter the plane of reflection (xy, yz, or xz): ").lower()
            transformed_shape = reflect_3d(shape, plane)
            plot_shape_3d(shape, transformed_shape, "Reflection")
        
        else:
            print("Invalid choice! Please choose between 1 and 4.")
    
    else:
        print("Invalid choice! Please choose between 1 (2D) and 2 (3D).")

if __name__ == "__main__":
    main()
