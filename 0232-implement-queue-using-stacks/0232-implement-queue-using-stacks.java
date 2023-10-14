class MyQueue {

    private Stack<Integer> dupliQ;
    private Stack<Integer> revStack;
    
    public MyQueue() {
        dupliQ = new Stack<>();;
        revStack = new Stack<>();
    }
    
    public void push(int x) {
        dupliQ.push(x);
    }
    
    public int pop() {
        while(!dupliQ.isEmpty())
            revStack.push(dupliQ.pop());
        int pop = revStack.pop();
        while(!revStack.isEmpty())
            dupliQ.push(revStack.pop());
        return pop;
    }
    
    public int peek() {
        while(!dupliQ.isEmpty())
            revStack.push(dupliQ.pop());
        int peek = revStack.peek();
        while(!revStack.isEmpty())
            dupliQ.push(revStack.pop());
        return peek;
    }
    
    public boolean empty() {
        return dupliQ.isEmpty();
    }
    
    
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */