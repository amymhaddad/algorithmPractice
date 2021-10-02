package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}


import "sort"


func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    
	s := []*TreeNode{}
	s = append(s, root)

	depth := 1
	var totalDepths []int

	//This check should be if s is empty -- not root, right?
	for root != nil {
		var curr *TreeNode
		curr, s = s[0], s[1:]

        if curr.Left == nil && curr.Right== nil {
			totalDepths =append(totalDepths, depth)
			depth = 1
            //need to reset the value here to traverse back up the tree; need to add a value to s (bc it could be empty )
            fmt.Println(root.Val, curr.Val)
		}
        
		if root.Left != nil {
            depth++
			s = append(s, root.Left)
			root = root.Left
		} else {
            fmt.Println(totalDepths, curr.Val)
            depth++
			s = append(s, root.Right)
			root = root.Right
		}
		
	}
	sort.Ints(totalDepths)
	return totalDepths[0]
}
