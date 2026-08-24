from tkinter import *
from tkinter import messagebox

# 컴퓨터 용어와 설명을 저장하는 딕셔너리입니다.
# 딕셔너리는 '키: 값' 형태로 자료를 저장합니다.
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다.",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용할 수 있습니다.",
    "CPU": "중앙 처리 장치의 약자로, 컴퓨터의 두뇌에 해당하는 부품입니다.",
    "RAM": "컴퓨터가 작업하는 동안 데이터를 임시로 저장하는 메모리입니다.",
}


def normalize_word(word):
    """입력한 용어의 앞뒤 공백을 제거하고 영어는 대문자로 바꿉니다."""
    return word.strip().upper()


def search():
    """입력한 용어를 사전에서 찾아 설명을 보여 줍니다."""
    word = normalize_word(search_entry.get())

    if not word:
        output.delete("1.0", END)
        output.insert(END, "검색할 용어를 입력하세요.")
        return

    # get()은 용어가 없을 때 두 번째 값을 대신 사용합니다.
    meaning = dic.get(word, "사전에 없는 용어입니다.")

    # Text 위젯에 남아 있는 이전 결과를 지웁니다.
    output.delete("1.0", END)
    output.insert(END, f"{word}: {meaning}")


def add_word():
    """새 용어와 설명을 딕셔너리에 추가합니다."""
    word = normalize_word(word_entry.get())
    meaning = meaning_entry.get().strip()

    # 용어나 설명을 입력하지 않은 경우에는 추가하지 않습니다.
    if not word or not meaning:
        messagebox.showwarning("입력 확인", "용어와 설명을 모두 입력하세요.")
        return

    # 이미 등록된 용어를 실수로 덮어쓰지 않도록 확인합니다.
    if word in dic:
        messagebox.showwarning("중복 용어", "이미 등록된 용어입니다.")
        return

    # 딕셔너리에 새 용어와 설명을 저장합니다.
    dic[word] = meaning

    # 추가가 끝났으므로 입력칸을 비웁니다.
    word_entry.delete(0, END)
    meaning_entry.delete(0, END)
    messagebox.showinfo("추가 완료", f"'{word}' 용어가 추가되었습니다.")


# 프로그램의 기본 창을 만듭니다.
window = Tk()
window.title("컴퓨터 용어 사전")
window.resizable(False, False)

# 검색 영역
Label(window, text="검색할 용어:").grid(
    row=0, column=0, sticky=W, padx=10, pady=(10, 3)
)
search_entry = Entry(window, width=40)
search_entry.grid(row=1, column=0, padx=10, pady=3)
Button(window, text="검색", width=10, command=search).grid(
    row=1, column=1, padx=(0, 10), pady=3
)

# 검색 결과를 여러 줄로 보여 주는 Text 위젯입니다.
output = Text(window, width=55, height=5)
output.grid(row=2, column=0, columnspan=2, padx=10, pady=(3, 12))

# 새 용어 추가 영역
Label(window, text="새 용어 추가", font=("맑은 고딕", 11, "bold")).grid(
    row=3, column=0, columnspan=2, sticky=W, padx=10, pady=(0, 5)
)
Label(window, text="용어:").grid(row=4, column=0, sticky=W, padx=10, pady=3)
word_entry = Entry(window, width=40)
word_entry.grid(row=5, column=0, padx=10, pady=3)

Label(window, text="설명:").grid(row=6, column=0, sticky=W, padx=10, pady=3)
meaning_entry = Entry(window, width=40)
meaning_entry.grid(row=7, column=0, padx=10, pady=3)
Button(window, text="새 용어 추가", width=15, command=add_word).grid(
    row=7, column=1, padx=(0, 10), pady=3
)

# 엔터 키를 누르면 검색 버튼을 누른 것처럼 동작합니다.
search_entry.bind("<Return>", lambda event: search())
meaning_entry.bind("<Return>", lambda event: add_word())

# 창을 닫을 때까지 프로그램을 실행합니다.
window.mainloop()
