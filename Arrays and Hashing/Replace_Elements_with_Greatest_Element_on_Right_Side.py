class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        arr.append(-1)   # Append -1 to the end of the list

        for i in range( len( arr ) - 1, 0, -1 ):
            if ( arr[i] > arr[i - 1] ):    # If the element at index i is greater than the element at index i - 1
                arr[i - 1] = arr[i]   # Replace the element at index i - 1 with the element at index i
        return arr[1:]   # Return the list from index 1 to the end of the list