###############################################################################
# Octaprobe Security Scanner - Network Security Analysis Suite
# Secure, Scalable, Enterprise-Grade Scanning Infrastructure (atleast we try)
###############################################################################
# Licensed under the terms specified in the LICENSE file
# Built as a part of Osmania University- B.E Final Year Project
###############################################################################

import sqlite3


def conect_db():
    conn = sqlite3.connect("assets/data/octaprobe.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)
    
    conn.commit()
