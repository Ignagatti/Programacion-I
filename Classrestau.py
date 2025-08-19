self.mesas_reservadas = [False] * 12

        mesas_frame = Frame(self.ventana, bg=fondo)
        mesas_frame.pack(pady=40)

        self.botones_mesas = []
        mesa_num = 1
        for fila in range(3):
            for columna in range(4):
                color = "#E0FFE0" if not self.mesas_reservadas[mesa_num - 1] else "#FF5C5C"
                if self.tipo == "Administrador":
                    boton = Button(
                        mesas_frame,
                        text=f"Mesa {mesa_num}",
                        width=12,
                        height=4,
                        font=("Arial", 12),
                        bg=color,
                        command=lambda n=mesa_num: self.editar_mesa(n)
                    )
                else:
                    boton = Button(
                        mesas_frame,
                        text=f"Mesa {mesa_num}",
                        width=12,
                        height=4,
                        font=("Arial", 12),
                        bg=color,
                        command=lambda n=mesa_num: self.reservar_mesa(n)
                    )
                boton.grid(row=fila, column=columna, padx=10, pady=10)
                self.botones_mesas.append(boton)
                mesa_num += 1

    def reservar_mesa(self, numero):
        idx = numero - 1
        if self.mesas_reservadas[idx]:
            messagebox.showwarning("Mesa ocupada", f"La mesa {numero} ya está reservada.")
        else:
            self.mesas_reservadas[idx] = True
            self.botones_mesas[idx].configure(bg="#FF5C5C")
            messagebox.showinfo("Reserva", f"Reservaste la mesa {numero}")

    def editar_mesa(self, numero):
        idx = numero - 1
        if self.mesas_reservadas[idx]:
            # Opción para liberar la mesa
            if messagebox.askyesno("Liberar mesa", f"¿Deseas liberar la mesa {numero}?"):
                self.mesas_reservadas[idx] = False
                self.botones_mesas[idx].configure(bg="#E0FFE0")
        else:
            # Opción para reservar desde admin
            if messagebox.askyesno("Reservar mesa", f"¿Deseas reservar la mesa {numero}?"):
                self.mesas_reservadas[idx] = True
                self.botones_mesas[idx].configure(bg="#FF5C5C")