class Rectangle:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height
        
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2*self.width) + (2*self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2))**.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        #Create top line
        top_line = "*"*self.width
        output = top_line + "\n"
        start_col = 0
        end_col = self.width
        body_col = "*"*self.width
        body_rows = self.height - 2
        for r in range(0,body_rows,1):
            output += body_col + "\n"
        output += top_line + "\n"
        
        return output
    
    def get_amount_inside(self,target):
        #first check if shape will actually fit inside
        if self.width < target.width or self.height < target.height:
            return 0
        
        #determine the width of the target compared to the self
        w = self.width // target.width
        
        #determine the height of the target compared to the self
        h = self.height // target.height
        
        #Now multiply the values to determine how many times it can fit
        output = w * h
        
        return output



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side,height=side)
        
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self,side):
        self.width = side
        self.height = side
    