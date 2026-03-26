import tkinter as tk
from tkinter import messagebox
import random

# --- AI Knowledge Base (3D Matrix) ---
FOOD_DB = {
    "YOUTH": {
        "NON-VEG": [
            {"name": "HIGH-OCTANE CHICKEN BOWL", "cal": 850, "p": 50, "c": 90, "f": 25},
            {"name": "BEEF-TECH MASS GAINER", "cal": 950, "p": 55, "c": 100, "f": 30}
        ],
        "VEG": [
            {"name": "SYNTH-PANEER POWER-WRAP", "cal": 800, "p": 35, "c": 85, "f": 30},
            {"name": "LENTIL-MAX GROWTH BOWL", "cal": 750, "p": 30, "c": 95, "f": 20}
        ]
    },
    "ADULT": {
        "NON-VEG": [
            {"name": "CRYO-CHICKEN & GLUCO-RICE", "cal": 600, "p": 45, "c": 50, "f": 12},
            {"name": "OMEGA-3 SALMON & QUINOA", "cal": 700, "p": 38, "c": 40, "f": 22}
        ],
        "VEG": [
            {"name": "CHICKPEA PROTEIN-BOWL", "cal": 520, "p": 22, "c": 65, "f": 10},
            {"name": "TOFU-TECH GREEN STIR-FRY", "cal": 420, "p": 25, "c": 30, "f": 18}
        ]
    },
    "ELDER": {
        "NON-VEG": [
            {"name": "SOFT-BAKED SALMON MASH", "cal": 450, "p": 35, "c": 30, "f": 20},
            {"name": "TURKEY BONE-BROTH SOUP", "cal": 380, "p": 30, "c": 25, "f": 15}
        ],
        "VEG": [
            {"name": "LENTIL-CORE DAL & SOFT RICE", "cal": 400, "p": 18, "c": 55, "f": 8},
            {"name": "STEAMED GREENS & TOFU", "cal": 320, "p": 20, "c": 20, "f": 15}
        ]
    }
}


class AnimatedDietApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NEURAL-DIET v15.0 | FULL SYSTEM CALIBRATED")
        self.root.geometry("500x750")
        self.root.configure(bg="#050505")

        self.unit_mode = tk.StringVar(value="IMPERIAL")
        self.diet_mode = tk.StringVar(value="NON-VEG")

        self.setup_splash_screen()
        self.setup_input_screen()
        self.setup_result_screen()

        # Start Boot Sequence
        self.boot_text = "LOADING AGE-TIER HEURISTICS...\nCALIBRATING METABOLIC ENGINE...\nRENDERING UI OVERLAYS...\n> SYSTEM READY."
        self.type_char(0)

    # ==========================================
    # 1. SPLASH SCREEN
    # ==========================================
    def setup_splash_screen(self):
        self.splash_frame = tk.Frame(self.root, bg="#050505", width=500, height=750)
        self.splash_frame.place(x=0, y=0)
        self.splash_lbl = tk.Label(self.splash_frame, text="", font=("Consolas", 14, "bold"), fg="#00ffcc",
                                   bg="#050505", justify="left")
        self.splash_lbl.place(x=50, y=300)

    def type_char(self, index):
        if index < len(self.boot_text):
            self.splash_lbl.config(text=self.splash_lbl.cget("text") + self.boot_text[index])
            self.root.after(30, self.type_char, index + 1)
        else:
            self.root.after(800, self.end_splash)

    def end_splash(self):
        self.splash_frame.destroy()
        self.input_frame.place(x=0, y=0)
        # ONLY trigger the animation loop here, do not recreate the canvas!
        self.animate_background()

    # ==========================================
    # 2. INPUT SCREEN & BACKGROUND ENGINE
    # ==========================================
    def setup_input_screen(self):
        self.input_frame = tk.Frame(self.root, bg="#050505", width=500, height=750)

        # --- LAYER 0: BACKGROUND CANVAS ---
        self.bg_canvas = tk.Canvas(self.input_frame, width=500, height=750, bg="#050505", highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)  # Placed first so it stays at the bottom

        self.particles = []
        for _ in range(50):  # Matrix particles
            p_id = self.bg_canvas.create_text(random.randint(0, 500), random.randint(0, 750),
                                              text=random.choice(["0", "1", "+", "-"]),
                                              fill=random.choice(["#003322", "#004433", "#005544"]),
                                              font=("Consolas", 10))
            self.particles.append({"id": p_id, "vx": random.uniform(-0.5, 0.5), "vy": random.uniform(-1.0, -0.2)})
        self.scanline = self.bg_canvas.create_line(0, 0, 500, 0, fill="#00ffcc", width=2, stipple="gray50")

        # --- LAYER 1: UI WIDGETS ---
        # Because these are placed AFTER the canvas, Tkinter draws them on top!
        tk.Label(self.input_frame, text="[ NEURAL INPUT ]", font=("Consolas", 24, "bold"), fg="#00ffcc",
                 bg="#050505").place(x=110, y=40)

        tk.Button(self.input_frame, textvariable=self.unit_mode,
                  command=lambda: self.unit_mode.set("METRIC" if self.unit_mode.get() == "IMPERIAL" else "IMPERIAL"),
                  bg="#111", fg="#fff", width=12, font=("Consolas", 10), relief="flat").place(x=100, y=120)

        tk.Button(self.input_frame, textvariable=self.diet_mode,
                  command=lambda: self.diet_mode.set("VEG" if self.diet_mode.get() == "NON-VEG" else "NON-VEG"),
                  bg="#111", fg="#fff", width=12, font=("Consolas", 10), relief="flat").place(x=300, y=120)

        self.vars = {}
        y_pos = 200
        for label, key, hint in [("BODY MASS", "w", "180"), ("HEIGHT", "h", "5'9"), ("BIO-AGE", "a", "Min 14")]:
            tk.Label(self.input_frame, text=label, font=("Consolas", 10), fg="#00ffcc", bg="#050505").place(x=200,
                                                                                                            y=y_pos)
            ent = tk.Entry(self.input_frame, font=("Consolas", 16), bg="#111", fg="white", insertbackground="#00ffcc",
                           borderwidth=1, justify="center")
            ent.place(x=125, y=y_pos + 25, width=250, height=40)
            ent.insert(0, hint)
            self.vars[key] = ent
            y_pos += 100

        tk.Button(self.input_frame, text="INITIATE SCAN", command=self.run_ai, font=("Consolas", 16, "bold"),
                  bg="#00ffcc", fg="black", relief="flat").place(x=125, y=550, width=250, height=50)

    def animate_background(self):
        # Keeps the background moving
        for p in self.particles:
            self.bg_canvas.move(p["id"], p["vx"], p["vy"])
            coords = self.bg_canvas.coords(p["id"])
            if coords[1] < -10: self.bg_canvas.move(p["id"], 0, 770)
            if coords[0] < -10: self.bg_canvas.move(p["id"], 520, 0)
            if coords[0] > 510: self.bg_canvas.move(p["id"], -520, 0)
        self.bg_canvas.move(self.scanline, 0, 3)
        if self.bg_canvas.coords(self.scanline)[1] > 750:
            self.bg_canvas.coords(self.scanline, 0, -10, 500, -10)
        self.root.after(30, self.animate_background)

    # ==========================================
    # 3. RESULT SCREEN & SLIDE LOGIC
    # ==========================================
    def setup_result_screen(self):
        self.result_frame = tk.Frame(self.root, bg="#050505", width=500, height=750)
        self.result_frame.place(x=500, y=0)  # Hidden off-screen right
        tk.Label(self.result_frame, text="[ PATHFOUND ]", font=("Consolas", 24, "bold"), fg="#00ffcc",
                 bg="#050505").place(x=130, y=40)

        self.terminal = tk.Text(self.result_frame, font=("Consolas", 12), bg="#000", fg="#00ffcc", borderwidth=1,
                                highlightbackground="#00ffcc", padx=20, pady=20)
        self.terminal.place(x=40, y=120, width=420, height=450)

        tk.Button(self.result_frame, text="< RETURN", command=self.slide_back, font=("Consolas", 14, "bold"), bg="#111",
                  fg="#00ffcc", relief="flat").place(x=150, y=600, width=200, height=50)

    def slide_forward(self, current_x=0):
        if current_x > -500:
            current_x -= 25
            self.input_frame.place(x=current_x, y=0)
            self.result_frame.place(x=current_x + 500, y=0)
            self.root.after(16, self.slide_forward, current_x)

    def slide_back(self, current_x=-500):
        if current_x < 0:
            current_x += 25
            self.input_frame.place(x=current_x, y=0)
            self.result_frame.place(x=current_x + 500, y=0)
            self.root.after(16, self.slide_back, current_x)

    # ==========================================
    # 4. CORE AI LOGIC (AGE CONSTRAINTS)
    # ==========================================
    def run_ai(self):
        try:
            # AGE CONSTRAINT & TIER ASSIGNMENT
            a = int(self.vars['a'].get())
            if a < 14:
                raise ValueError("AGE_MINIMUM_ERROR")

            if a <= 24:
                tier, met_multi = "YOUTH", 1.5
            elif a <= 55:
                tier, met_multi = "ADULT", 1.35
            else:
                tier, met_multi = "ELDER", 1.2

            w_val = float(self.vars['w'].get())
            w = w_val if self.unit_mode.get() == "METRIC" else w_val * 0.453

            h_in = self.vars['h'].get().strip()
            if "'" in h_in:
                p = h_in.split("'")
                h = ((int(p[0]) * 12) + (int(p[1]) if len(p) > 1 and p[1] else 0)) * 2.54
            else:
                h = float(h_in)
                if self.unit_mode.get() == "IMPERIAL": h *= 30.48

                # DYNAMIC TDEE CALCULATION
            tdee = ((10 * w) + (6.25 * h) - (5 * a) + 5) * met_multi
            target = tdee * 0.45

            # ROUTING TO THE CORRECT DATABASE TIER
            pool = FOOD_DB[tier][self.diet_mode.get()]
            best = random.choice(sorted(pool, key=lambda x: abs(x['cal'] - target))[:2])

            self.terminal.delete("1.0", tk.END)
            self.terminal.insert(tk.END, f"AGE TIER ASSIGNED: [{tier}]\n")
            self.terminal.insert(tk.END, f"METABOLIC MULTIPLIER: {met_multi}x\n")
            self.terminal.insert(tk.END, f"{'-' * 30}\n")
            self.terminal.insert(tk.END, f"BIOMETRICS: {w:.1f}kg | {h:.1f}cm\n")
            self.terminal.insert(tk.END, f"ADJUSTED TDEE: {int(tdee)} KCAL\n")
            self.terminal.insert(tk.END, f"{'-' * 30}\n\n")
            self.terminal.insert(tk.END, f"OPTIMAL {tier} MEAL:\n{best['name']}\n\n")
            self.terminal.insert(tk.END, f"ENERGY: {best['cal']} KCAL\n")
            self.terminal.insert(tk.END, f"MACROS: P:{best['p']}g | C:{best['c']}g | F:{best['f']}g\n")

            self.slide_forward()

        except ValueError as e:
            if str(e) == "AGE_MINIMUM_ERROR":
                messagebox.showerror("RESTRICTED", "BIO-AGE MUST BE >= 14 FOR ACCURATE MODELING.")
            else:
                messagebox.showerror("ERROR", "Invalid Input. Use numbers (e.g., 180, 5'9, 22)")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedDietApp(root)
    root.mainloop()