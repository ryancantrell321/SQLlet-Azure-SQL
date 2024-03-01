from src.mechanisms.button_mechanisms import *
from src.miscellaneous.fonts import font1
from src.miscellaneous.time import *
from src.mechanisms.entry_field_mechanisms import toggle_password_visibility


def test_button(self, x_position, y_position, w, c):
    tb = ctk.CTkButton(master=self.master, width=w, text="Test Connection", font=font1,
                       fg_color="#b3b3b3", bg_color="#010119", hover_color="grey", text_color="black",
                       command=lambda: c(self))
    tb.place(x=x_position, y=y_position)


def reset_button(self, x_position, y_position, w, c):
    rb = ctk.CTkButton(master=self.master, width=w, text="Reset Fields", font=font1,
                       fg_color="#b3b3b3", bg_color="black", hover_color="grey", text_color="black",
                       command=lambda: c(self))
    rb.place(x=x_position, y=y_position)


def help_button(self, x_position, y_position, w, c):
    hb = ctk.CTkButton(master=self.master, width=w, text="Help", font=font1,
                       fg_color="#b3b3b3", bg_color="black", hover_color="grey", text_color="black",
                       command=lambda: c(self))
    hb.place(x=x_position, y=y_position)


def install_button(self, x_position, y_position, w, c):
    ib = ctk.CTkButton(master=self.master, width=w, text="Install Driver",
                       font=font1, fg_color="#b3b3b3", bg_color="black", text_color="black",
                       hover_color="grey", command=lambda: c(self))
    ib.place(x=x_position, y=y_position)


def about_button(self, x_position, y_position, w, c):
    ab = ctk.CTkButton(master=self.master, width=w, text="About",
                       font=font1, fg_color="#b3b3b3", bg_color="black", text_color="black",
                       hover_color="grey", command=lambda: c(self))
    ab.place(x=x_position, y=y_position)


def exit_button(self, x_position, y_position, w, c):
    eb = ctk.CTkButton(master=self.master, width=w, text="Exit", font=font1,
                       fg_color="#b3b3b3", bg_color="black", hover_color="grey", text_color="black",
                       command=lambda: c(self))
    eb.place(x=x_position, y=y_position)


def footer(self, x_position, y_position, w):
    cp_text = f"© {year()} PANDORA DYNAMICS. All Rights Reserved."
    ft = ctk.CTkLabel(master=self.master, width=w, text=cp_text, fg_color="#00394d")
    ft.place(x=x_position, y=y_position)


def checkbox(self, x_co_ordinate, y_co_ordinate, checkbox_width, w):
    self.show_password_var = tk.BooleanVar()
    self.show_password_var.set(False)

    show_pwd_checkbox = ctk.CTkCheckBox(self.master, text="SHOW", variable=self.show_password_var,
                                        checkbox_width=checkbox_width, width=w, bg_color="black", fg_color="#005e80",
                                        hover_color="#00a8e6", command=lambda: toggle_password_visibility(self))
    show_pwd_checkbox.place(x=x_co_ordinate, y=y_co_ordinate)