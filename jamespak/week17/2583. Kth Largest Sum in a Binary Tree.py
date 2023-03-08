class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:

        queue, ans = deque([root]), []

        while len(queue) > 0:
            count = 0

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

                count += node.val

            ans.append(count)

        return sorted(ans)[-k] if k <= len(ans) else -1
