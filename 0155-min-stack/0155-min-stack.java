class MinStack {
    Stack<Integer> minStack;
    Stack<Integer> minSoFar;
    
    public MinStack() {
        minStack = new Stack();
        minSoFar = new Stack();
        
    }
    
    public void push(int val) {
        if(minSoFar.size() == 0){
            minSoFar.push(val);
        }
        else{
            minSoFar.push(Math.min(val, minSoFar.peek()));
        }
        minStack.push(val);
        
    }
    
    public void pop() {
        minSoFar.pop();
        minStack.pop();
        
    }
    
    public int top() {
        return minStack.peek();
        
    }
    
    public int getMin() {
        return minSoFar.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */