import os
from selenium import webdriver
import time
import logging
import sys
import inspect


def get_script_dir(follow_symlinks=True):
    if getattr(sys, "frozen", False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def skip_intro(browser):
    while True:
        time.sleep(1)
        try:
            btn_skip_intro = browser.find_element_by_css_selector(
                ".vjs-overlay.vjs-overlay-bottom-left.vjs-overlay-skip-intro.vjs-overlay-background"
            )
            time.sleep(4)
            btn_skip_intro.click()
        except:
            pass
        else:
            break


def skip_outro(browser):
    while True:
        time.sleep(1)
        try:
            btn_skip_outro = browser.find_element_by_css_selector(
                ".vjs-overlay.vjs-overlay-bottom-right.vjs-overlay-skip-intro.vjs-overlay-background"
            )
            time.sleep(4)
            btn_skip_outro.click()
        except:
            pass
        else:
            break


def full_hd_quality(browser):
    while True:
        time.sleep(1)
        try:
            btn_quality = browser.find_element_by_css_selector(
                ".vjs-quality-selector.vjs-menu-button.vjs-menu-button-popup.vjs-control.vjs-button"
            )
            btn_quality.click()
            time.sleep(4)
            qualty_fullhd = browser.find_elements_by_css_selector(
                ".vjs-menu-item-text"
            )[1]
            qualty_fullhd.click()
        except:
            pass
        else:
            break


def main():
    try:
        extension_location = f"{get_script_dir()}\\uBlock0_1.38.6.firefox.xpi"
        browser = webdriver.Firefox()
        browser.install_addon(extension_location, temporary=True)
        browser.maximize_window()
        url = input("url: ")

        browser.get(url)
        last_url = ""
        while True:
            time.sleep(1)
            try:
                btn = browser.find_element_by_class_name("vjs-big-play-button")
                btn.click() 
                btn_fullscreen = browser.find_element_by_css_selector(
                    ".vjs-fullscreen-control"
                )
                btn_fullscreen.click()
                if last_url != browser.current_url:
                    skip_intro(browser)
                    last_url = browser.current_url
                    logging.info(f"{browser.current_url}")

                skip_outro(browser)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


# 238
if __name__ == "__main__":
    logging.basicConfig(
        filename=f"{get_script_dir()}\\auto_player.log",
        format="%(asctime)s - %(message)s",
        level=logging.INFO,
    )
    main()
