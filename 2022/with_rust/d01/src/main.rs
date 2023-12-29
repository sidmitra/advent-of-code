use std::fs;

fn main() {
    let filename = "input.txt";
    let content = fs::read_to_string(filename).expect("Something went wrong reading the file.");

    // max
    let sum: i32 = 0;
    let lines = content.lines();
    for line in lines {
        println!("{:?}", line);
    }
}
