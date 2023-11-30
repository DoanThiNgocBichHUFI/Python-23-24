#bieu dien vi tri cua trang thai
class State:
    def __init__(self, position):
        self.position = position
#nhan vao trang thai hien tai, và trả về danh sách các trạng thái sau khi mở rộng theo tất cả các hướng có thể di chuyển.
def expand_state(current_state):
    possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Các hướng di chuyển: phải, xuống, trái, lên

    expanded_states = []
     #lấy giá trị của 1 hg di chuyển có thể xảy ra 
    for move in possible_moves:
        new_position = (
            current_state.position[0] + move[0], # vị trí hiện tại của trạng thái, move[0] và move[1] lần lượt là phần tử thứ nhất và thứ hai của tuple move, biểu diễn cho sự thay đổi theo chiều ngang và chiều dọc.
            current_state.position[1] + move[1]
        )

        new_state = State(new_position) #vị trí mới
        expanded_states.append(new_state)

    return expanded_states

# Ví dụ sử dụng
initial_state = State((0, 0))
expanded_states = expand_state(initial_state)

print("Trạng thái ban đầu:", initial_state.position)
print("Các trạng thái sau khi mở rộng:")
for state in expanded_states:
    print(state.position)
