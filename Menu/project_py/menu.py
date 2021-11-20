from shape_classification import find_circle, find_sqr_rect, find_triangle, find_pentagon, find_hexagon
from Img_tensorflow import tensorflow
from shape_size import shape_size
from size_shape import size_shape
from size import size
from shape import shape
from webcam import camera
from video import video

def main_menu():

    loop = True 

    while loop:
        print("\n\t Options :")
        print( """
                  1. Shape Classification
                  2. Face Detection TensorFlow
                  3. Sort by shape the size
                  4. Sort by size then shape
                  5. Sort by size
                  6. Sort by shape
                  7. Face recognition (webcam)
                  8. Face recognition (video)
                  9. Exit
                """)

        choice = input("Enter your choice: ")

        if choice == '1':
            user_input = input("""Options:
                        a : to classify Squares and Rectangles\n 
                        b : to classify Triangles\n  
                        c : to classify Pentagons\n
                        d : to classify Cirles\n
                        e : to classify Hexagon\n

                        Answer: """)

            if user_input == 'a' :
                find_sqr_rect('../data/shape3.png')
            elif user_input == 'b':
                find_triangle('../data/shape3.png')
            elif user_input == 'c':
                find_pentagon('../data/shape3.png')
            elif user_input == 'd':
                find_circle('../data/shape3.png')
            elif user_input == 'e':
                find_hexagon('../data/shape3.png')
                                    
            
        elif choice == '2':
            tensorflow('../data/people.jpg')

        elif choice == '3':
            shape_size("../data/shape3.png")

        elif choice == '4':
            size_shape("../data/shape3.png")
        
        elif choice == '5':
            size("../data/shape3.png")
        
        elif choice == '6':
            shape("../data/shape3.png")

        elif choice == '7':
            camera(0)

        elif choice =='8':
            video('../data/video.mov')

        elif choice == '9':
            break
        
        else:
            print("Invalid entry")
            

            return choice


if __name__ == "__main__":
   choice = main_menu()

