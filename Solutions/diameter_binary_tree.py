def diameter(root):
  ## Time complexity O(N)
  ## Space complexity O(1)
  result=0
  
  def dfs(root):
    
    if root==None:
      return -1
    
    left= dfs(root.left)
    right=dfs(root.right)
    
    
    result= max(result,left+right+2)
    
    
    return 1+max(root.left,root.right)
  
  
  result= dfs(root)
  
  
  return result
