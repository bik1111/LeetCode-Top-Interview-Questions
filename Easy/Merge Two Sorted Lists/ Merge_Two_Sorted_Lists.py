from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 객체 초기화 (None)
        cur = dummy = ListNode()
        # 둘 다 None이 아니면
        while list1 and list2:
            # list1이 더 작으면
            if list1.val < list2.val:
                # cur이 list1을 바라보게 하고
                cur.next = list1
                # list1은 자식 한 명 내보냈으니 다음 자식으로 이동
                list1 , cur = list1.next , list1

            else:
                # list2가 더 작으면 cur의 다음 노드를 list2로 설정
                cur.next = list2
                # list2는 자식 한 명 내보냈으니 다음 자식으로 이동
                # cur은 다음 숫자를 추가하기 위해 list2로 업데이트
                # 원래 list2자리를 cur에게 내어줘야 끝에 계속 숫자를 붙일 수 있음.
                # 즉, cur은 항상 현재 병합된 리스트의 "끝" 노드를 가리키도록 업데이트
                list2, cur = list2.next, list2


        # 둘 중 하나라도 남아있으면
        if list1 or list2:
            cur.next = list1 if list1 else list2

        # dummy와 cur은 함께 초기화 되었기에, dummy의 next는 cur을 바라보게함
        # 실제로 연결 리스트의 시작 부분인 첫 번째 노드를 반환
        return dummy.next
