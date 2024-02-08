from src.mechanisms.button_mechanisms import *
from src.miscellaneous.fonts import font1
from src.miscellaneous.time import *
from src.mechanisms.entry_field_mechanisms import toggle_password_visibility


def test_button(self, x_position, y_position, w, c):
    tb = ctk.CTkButton(master=self.master, width=w, text="TEST CONNECTION", font=font1,
                       fg_color="#004d1a", bg_color="#010119", hover_color="#003311",
                       command=lambda: c(self))
    tb.place(x=x_position, y=y_position)


def reset_button(self, x_position, y_position, w, c):
    rb = ctk.CTkButton(master=self.master, width=w, text="RESET", font=font1,
                       fg_color="#66001a", bg_color="black", hover_color="#33000d",
                       command=lambda: c(self))
    rb.place(x=x_position, y=y_position)


def help_button(self, x_position, y_position, w, c):
    hb = ctk.CTkButton(master=self.master, width=w, text="HELP", font=font1,
                       fg_color="#1a0033", bg_color="black", hover_color="#330066",
                       command=lambda: c(self))
    hb.place(x=x_position, y=y_position)


def license_button(self, x_position, y_position, w, c):
    lb = ctk.CTkButton(master=self.master, width=w, text="LICENSE", font=font1,
                       fg_color="#93931f", bg_color="black", hover_color="#b3b300",
                       command=lambda: c(self))
    lb.place(x=x_position, y=y_position)


def install_button(self, x_position, y_position, w, c):
    ib = ctk.CTkButton(master=self.master, width=w, text="INSTALL DRIVER",
                       font=font1, fg_color="#994f00", bg_color="black",
                       hover_color="#804200", command=lambda: c(self))
    ib.place(x=x_position, y=y_position)


def about_button(self, x_position, y_position, w, c):
    ab = ctk.CTkButton(master=self.master, width=w, text="ABOUT",
                       font=font1, fg_color="#993366", bg_color="black",
                       hover_color="#73264d", command=lambda: c(self))
    ab.place(x=x_position, y=y_position)


def exit_button(self, x_position, y_position, w, c):
    eb = ctk.CTkButton(master=self.master, width=w, text="EXIT", font=font1,
                       fg_color="#005e80", bg_color="black", hover_color="#00384d",
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
