fn main() {
  // Array to sort
  let array = [3, 6, 12, 14, 3, 45];
  println!("Input array: {:?}", array);
  

  let merge_array = merge_sort(array);
  println!("Merged array: {:?}", merge_array);
}


fn merge_sort(arr: [i32; 6]) -> [i32; 3] {
  let bottom_half_array =&arr[0..3];
  println!("Subset bottom half array: {:?}", bottom_half_array);
  let bottom_half_array_length = bottom_half_array.len(); // Get the length of the array
  println!("The length of the array is: {}", bottom_half_array_length); // Print the length

  let top_half_array =&arr[3..6];
  println!("Subset top half array: {:?}", top_half_array);
  let top_half_array_length = top_half_array.len(); // Get the length of the array
  println!("The length of the array is: {}", top_half_array_length); // Print the length

  let return_vector = bottom_half_array_length;
//   return arr;
  return return_vector;
}

// fn main() {
//     let my_array = [10, 20, 30, 40, 50]; // Define an array
//     let array_length = my_array.len(); // Get the length of the array

//     println!("The length of the array is: {}", array_length); // Print the length
// }

// fn main() {
//     let source_array = [10, 20, 30, 40, 50];
//     let mut target_array = [0; 7]; // Initialize with zeros

//     // Assign the entire source_array to a subset of target_array
//     // target_array[1..6] will be assigned the values from source_array
//     target_array[1..6].copy_from_slice(&source_array); 
//     println!("Target array after full copy: {:?}", target_array); // Output: [0, 10, 20, 30, 40, 50, 0]

//     // Assign a subset of source_array to a subset of target_array
//     let source_subset = &source_array[1..4]; // [20, 30, 40]
//     target_array[3..6].copy_from_slice(source_subset);
//     println!("Target array after subset copy: {:?}", target_array); // Output: [0, 10, 20, 20, 30, 40, 0]
// }