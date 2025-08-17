# ============================================================
# 📜 Copyright Notice
#
# This script is the intellectual property of its author.
# It is provided for free for personal or educational use.
#
# ❌ It is strictly forbidden to:
#    - sell this script or any part of it,
#    - distribute it without permission,
#    - modify it for commercial purposes.
#
# ✅ You are allowed to:
#    - use it freely for personal use,
#    - modify it for private/non-commercial use.
#
# Please respect the author's work.
# ============================================================

import pyfiglet
from termcolor import colored
import os
import sys

class AsciiArtGenerator:
    def __init__(self):
        self.fonts = [
            'standard', 'slant', 'big', 'block', 'bubble', 'digital', 
            'bloody', 'doh', 'larry3d', 'letters', 'mini', 'script',
            'smscript', 'starwars', 'sub-zero', 'univers', '3-d', 
            '3x5', '5lineoblique', 'alligator', 'banner', 'banner3',
            'big_money', 'broadway', 'bulbhead', 'calgphy2', 'caligraphy',
            'chunky', 'colossal', 'contessa', 'cyberlarge', 'cybermedium',
            'doom', 'epic', 'fender', 'fuzzy', 'georgi16', 'georgia11',
            'ghost', 'gothic', 'graceful', 'greek', 'heart_left',
            'heart_right', 'hex', 'hieroglyphs', 'hollywood', 'invita',
            'isometric1', 'isometric2', 'isometric3', 'isometric4',
            'italic', 'jazmine', 'jerusalem', 'katakana', 'lean',
            'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour',
            'mike', 'morse', 'moscow', 'nancyj', 'nancyj-fancy',
            'nancyj-underlined', 'nipples', 'ntgreek', 'o8', 'ogre',
            'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy',
            'pyramid', 'rectangles', 'relief', 'relief2', 'rev',
            'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'rustofat',
            'santa_clara', 'shadow', 'short', 'slscript', 'small',
            'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant',
            'smtengwar', 'speed', 'stampatello', 'standard', 'star_wars',
            'stellar', 'stop', 'straight', 'tanja', 'tengwar',
            'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
            'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint',
            'univers', 'usaflag', 'weird'
        ]
        
        self.colors = [
            'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def center_text(self, text, width=80):
        lines = text.split('\n')
        centered_lines = []
        for line in lines:
            if line.strip():
                padding = max(0, (width - len(line)) // 2)
                centered_lines.append(' ' * padding + line)
            else:
                centered_lines.append('')
        return '\n'.join(centered_lines)

    def print_banner(self):
        self.clear_screen()
        
        banner = pyfiglet.figlet_format("ASCII GENERATOR", font='doom')
        print(colored(self.center_text(banner), 'cyan', attrs=['bold']))
        print(colored(self.center_text("v1.0 - Transform Text to ASCII Art"), 'yellow', attrs=['bold']))
        print(colored(self.center_text("═" * 60), 'magenta'))

    def display_fonts_grid(self):
        print(colored(self.center_text("\n🎨 AVAILABLE FONTS"), 'green', attrs=['bold']))
        print(colored(self.center_text("─" * 40), 'green'))
        
        fonts_per_row = 4
        colors = ['cyan', 'yellow', 'magenta', 'blue']
        
        for i in range(0, len(self.fonts), fonts_per_row):
            row_fonts = self.fonts[i:i+fonts_per_row]
            formatted_row = ""
            
            for j, font in enumerate(row_fonts):
                color = colors[j % len(colors)]
                if j == 0:
                    formatted_row = colored(f"{font:<18}", color)
                else:
                    formatted_row += colored(f"│ {font:<18}", color)
            
            print(self.center_text(formatted_row))

    def display_colors(self):
        print(colored(self.center_text("\n🌈 AVAILABLE COLORS"), 'white', attrs=['bold']))
        print(colored(self.center_text("─" * 40), 'white'))
        
        color_line = ""
        for i, color in enumerate(self.colors):
            if i == 0:
                color_line = colored(f"{color:<10}", color, attrs=['bold'])
            else:
                color_line += colored(f"│ {color:<10}", color, attrs=['bold'])
        
        print(self.center_text(color_line))

    def generate_ascii_art(self, text, font, color):
        try:
            if font not in self.fonts:
                print(colored(self.center_text("❌ Font not found! Using 'standard'"), 'red'))
                font = 'standard'
            
            if color not in self.colors:
                print(colored(self.center_text("❌ Color not found! Using 'cyan'"), 'red'))
                color = 'cyan'
            
            ascii_art = pyfiglet.figlet_format(text, font=font)
            
            print(colored(self.center_text(f"\n🎯 RESULT - Font: {font} | Color: {color}"), 'white', attrs=['bold']))
            print(colored(self.center_text("═" * 50), 'white'))
            
            print(colored(self.center_text(ascii_art), color, attrs=['bold']))
            
        except Exception as e:
            print(colored(self.center_text(f"❌ Error generating ASCII: {e}"), 'red'))

    def preview_font(self, font):
        if font not in self.fonts:
            print(colored(self.center_text("❌ Font not found!"), 'red'))
            return
        
        try:
            preview = pyfiglet.figlet_format("PREVIEW", font=font)
            print(colored(self.center_text(f"\n👀 FONT PREVIEW - {font}"), 'yellow', attrs=['bold']))
            print(colored(self.center_text("─" * 30), 'yellow'))
            print(colored(self.center_text(preview), 'cyan'))
        except:
            print(colored(self.center_text("❌ Cannot preview this font"), 'red'))

    def main_menu(self):
        while True:
            self.print_banner()
            
            print(colored(self.center_text("\n🎯 MAIN MENU"), 'white', attrs=['bold']))
            print(colored(self.center_text("─" * 30), 'white'))
            
            menu_items = [
                "[ 1 ] Generate ASCII Art",
                "[ 2 ] Show All Fonts", 
                "[ 3 ] Show All Colors",
                "[ 4 ] Preview Font",
                "[ 5 ] Batch Generate",
                "[ 0 ] Exit"
            ]
            
            colors = ['cyan', 'green', 'yellow', 'magenta', 'blue', 'red']
            
            for i, item in enumerate(menu_items):
                print(colored(self.center_text(item), colors[i % len(colors)], attrs=['bold']))
            
            print(colored(self.center_text("═" * 40), 'white'))
            
            choice = input(colored(self.center_text("🚀 Enter your choice: "), 'green', attrs=['bold'])).strip()
            
            if choice == '1':
                text = input(colored("Enter text to convert: ", 'cyan')).strip()
                if not text:
                    print(colored(self.center_text("❌ No text entered!"), 'red'))
                    input(colored(self.center_text("Press ENTER to continue..."), 'white'))
                    continue
                
                self.display_fonts_grid()
                font = input(colored("\nChoose font: ", 'yellow')).strip()
                
                self.display_colors()
                color = input(colored("\nChoose color: ", 'magenta')).strip()
                
                self.clear_screen()
                self.print_banner()
                self.generate_ascii_art(text, font, color)
                
            elif choice == '2':
                self.clear_screen()
                self.print_banner()
                self.display_fonts_grid()
                
            elif choice == '3':
                self.clear_screen()
                self.print_banner()
                self.display_colors()
                
            elif choice == '4':
                font = input(colored("Enter font name to preview: ", 'cyan')).strip()
                self.clear_screen()
                self.print_banner()
                self.preview_font(font)
                
            elif choice == '5':
                text = input(colored("Enter text for batch generation: ", 'cyan')).strip()
                if text:
                    self.clear_screen()
                    self.print_banner()
                    
                    popular_fonts = ['standard', 'slant', 'big', 'block', 'bubble', 'digital']
                    popular_colors = ['red', 'green', 'yellow', 'cyan', 'magenta']
                    
                    print(colored(self.center_text("🔥 BATCH GENERATION"), 'yellow', attrs=['bold']))
                    print(colored(self.center_text("═" * 40), 'yellow'))
                    
                    for font in popular_fonts:
                        for color in popular_colors[:2]:
                            try:
                                ascii_art = pyfiglet.figlet_format(text, font=font)
                                print(colored(self.center_text(f"\n{font} - {color}:"), 'white', attrs=['bold']))
                                print(colored(self.center_text(ascii_art), color, attrs=['bold']))
                            except:
                                pass
                
            elif choice == '0':
                self.clear_screen()
                print(colored(self.center_text("👋 Thanks for using ASCII Generator!"), 'green', attrs=['bold']))
                sys.exit(0)
                
            else:
                print(colored(self.center_text("❌ Invalid choice!"), 'red'))
            
            input(colored(self.center_text("\n⏸️ Press ENTER to continue..."), 'white', attrs=['bold']))

if __name__ == '__main__':
    try:
        generator = AsciiArtGenerator()
        generator.main_menu()
    except KeyboardInterrupt:
        print(colored("\n👋 Goodbye!", 'green', attrs=['bold']))
    except Exception as e:
        print(colored(f"\n❌ Error: {e}", 'red'))

# By @dldml, 2025. All rights reserved.
# ============================================================