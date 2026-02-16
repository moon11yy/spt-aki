import os
import shutil

BASE_DIR = os.getcwd()  # папка, откуда запущен скрипт

PLAN = {
    "Ammo": [
        "new45APCAPM.json",
        "new46x30_APSXM2.json",
        "new127x55_PS12C.json",
        "new300_NIFLHEIM.json",
        "new300_Spartan.json",
        "newM67RD.json",
        "newV40.json",
    ],

    "Armor": "__DELETE_FOLDER__",

    "Attachments": [
        "newAK74_GasTube.json",
        "newBS_AR15_DD_Enhanced_Collapsible_Buttstocks.json",
        "newGH_AK_Zenit_B30_.json",
        "newHG_SOK_12_Chaos_Quad_Rail.json",
        "newHG_SOK_12_Chaos_Titan_Quad_Rail_top_cover.json",
        "newMAG_300_Magpul_PMAG.json",
        "newMAG_4.6x.30mm_for_the_MPX46.json",
        "newMAG_556x45_300_STANAG_MAG5.json",
        "newMAG_762x54R_20_round_for_AK54R.json",
        "newMAG_762x54R_24_round_for_AK54R_2.json",
        "newMAG_9x39mm_for_the_MCX_939.json",
        "newNL762DI_Receiver.json",
        "newNL762GP_Receiver.json",
        "newPG_AK_Strike_Industries.json",
        "newSOK_12_Chaos_Titan_receiver_top_rail.json",
        "newSPEAR_16_Barrel.json",
        "newSPEAR_Receiver.json",
        "newSR25_Receiver.json",
        "newSUP_SureFire_Socom_556.json",
    ],

    "Config": "__DELETE_FOLDER__",

    "Items": [
        "newAzimut_SS_Zhuk_Chest_Harness_Black.json",
        "newBEAR_Armband_Container - Kopie.json",
        "newDynaforce_Triton_MPPV_vest.json",
        "newUSEC_Armband_Container.json",
    ],

    "Recipes": [
        "craft_300_Spartan.json",
        "craft_68x51_Berserker.json",
        "craft_GAC_4sss2_balistic_plate.json",
        "craft_Korund_VM_back.json",
        "craft_Korund_VM_front.json",
        "craft_M67RD.json",
        "craft_MAG_556x45_300_Magpul_PMAG.json",
        "craft_MAG_556x45_300_SureFire_MAG_STANAG.json",
        "craft_V40.json",
    ],
}


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        print(f"[DEL FILE] {path}")
    else:
        print(f"[SKIP] file not found: {path}")


def delete_folder(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"[DEL FOLDER] {path}")
    else:
        print(f"[SKIP] folder not found: {path}")


for folder, action in PLAN.items():
    full_path = os.path.join(BASE_DIR, folder)

    if action == "__DELETE_FOLDER__":
        delete_folder(full_path)
        continue

    for filename in action:
        delete_file(os.path.join(full_path, filename))

print("\nГотово.")
input("\nНажми Enter для выхода...")
