import os
from supabase import create_client, Client

# Supabase Bilgileri
SUPABASE_URL = "https://joqondoravzkeynrubsr.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpvcW9uZG9yYXZ6a2V5bnJ1YnNyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE1NTY3NjIsImV4cCI6MjA5NzEzMjc2Mn0.6BwOB2RIM8aGbKUjPawXbMTxyTrG6fuHu5nhW_NJGg4"

# Bağlantıyı Başlat
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def tum_kullanicilari_getir():
    """Veritabanındaki tüm kullanıcıları listeler"""
    try:
        response = supabase.table("users").select("*").execute()
        print("\n--- AtlantisMC Kayıtlı Kullanıcılar ---")
        for user in response.data:
            admin_durumu = "👑 Admin" if user['is_admin'] else "👤 Üye"
            print(f"Kullanıcı Adı: @{user['handle']} | İsim: {user['name']} | Rol: {admin_durumu}")
    except Exception as e:
        print("Hata oluştu:", e)

def yeni_sistem_duyurusu_yap(mesaj_metni):
    """Sistem adına (atlantis hesabı) otomatik duyuru postu paylaşır"""
    veri = {
        "user_handle": "atlantis",
        "text": mesaj_metni,
        "category": "duyuru"
    }
    response = supabase.table("posts").insert(veri).execute()
    if response.data:
        print("\n🚀 Sistem duyurusu başarıyla veritabanına işlendi ve yayınlandı!")

def pasif_kullanicilari_temizle(kullanici_handle):
    """İstenmeyen veya kural ihlali yapan kullanıcıyı veritabanından siler (Postları da silinir)"""
    response = supabase.table("users").delete().eq("handle", kullanici_handle).execute()
    print(f"\n❌ {kullanici_handle} kullanıcısı ve ona ait tüm veriler veritabanından kaldırıldı.")

# ---- TEST ETME ALANI ----
if __name__ == "__main__":
    # 1. Mevcut kullanıcıları terminale yazdır
    tum_kullanicilari_getir()
    
    # 2. Python üzerinden otomatik duyuru gönder
    # yeni_sistem_duyurusu_yap("Sistem Güncellemesi: Sunucu altyapısı Supabase'e taşındı! 🌌")