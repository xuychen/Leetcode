class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        stack = []
        pop_ptr = 0

        for push_num in pushed:
            stack.append(push_num)

            while stack and stack[-1] == popped[pop_ptr]:
                stack.pop()
                pop_ptr += 1

        return not stack