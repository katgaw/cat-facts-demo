#!/usr/bin/env python3
"""
Cat Facts Generator
A simple script that prints interesting facts about cats.
"""

import random
import time

def print_cat_facts():
    """Print a collection of interesting cat facts."""
    
    cat_facts = [
        "🐱 Cats have been domesticated for over 4,000 years!",
        "🐱 A group of cats is called a 'clowder'.",
        "🐱 Cats spend 70% of their lives sleeping - that's 13-16 hours a day!",
        "🐱 A cat's purr vibrates at 25-150 Hz, which can help heal bones!",
        "🐱 Cats have a third eyelid called a 'nictitating membrane'.",
        "🐱 A cat's nose print is unique, just like human fingerprints!",
        "🐱 Cats can rotate their ears 180 degrees independently.",
        "🐱 The oldest known pet cat existed 9,500 years ago in Cyprus.",
        "🐱 Cats have over 30 muscles controlling their ears.",
        "🐱 A cat's heart beats twice as fast as a human's (110-140 bpm).",
        "🐱 Cats can jump up to 6 times their body length in a single bound!",
        "🐱 A cat's whiskers are roughly as wide as their body to help them navigate.",
        "🐱 Cats have a special reflective layer in their eyes called the 'tapetum lucidum'.",
        "🐱 The richest cat in the world inherited $13 million from its owner!",
        "🐱 Cats can make over 100 different sounds, while dogs only make about 10.",
        "🐱 A cat's brain is 90% similar to a human's brain!",
        "🐱 Cats don't have collarbones, which allows them to fit through any space their head can fit through.",
        "🐱 The first cat in space was French - her name was Félicette in 1963.",
        "🐱 Cats have scent glands on their paws, cheeks, and foreheads.",
        "🐱 A cat's tongue has tiny, hook-like structures that help them groom efficiently."
    ]
    
    print("=" * 60)
    print("🐾 WELCOME TO THE AMAZING CAT FACTS GENERATOR! 🐾")
    print("=" * 60)
    print()
    
    print("Here are some fascinating facts about our feline friends:")
    print()
    
    # Print 5 random facts
    selected_facts = random.sample(cat_facts, min(5, len(cat_facts)))
    
    for i, fact in enumerate(selected_facts, 1):
        print(f"{i}. {fact}")
        time.sleep(0.5)  # Small delay for dramatic effect
    
    print()
    print("=" * 60)
    print("🐱 Did you know all of these amazing cat facts? 🐱")
    print("=" * 60)

def print_random_fact():
    """Print a single random cat fact."""
    cat_facts = [
        "🐱 Cats have been domesticated for over 4,000 years!",
        "🐱 A group of cats is called a 'clowder'.",
        "🐱 Cats spend 70% of their lives sleeping - that's 13-16 hours a day!",
        "🐱 A cat's purr vibrates at 25-150 Hz, which can help heal bones!",
        "🐱 Cats have a third eyelid called a 'nictitating membrane'.",
        "🐱 A cat's nose print is unique, just like human fingerprints!",
        "🐱 Cats can rotate their ears 180 degrees independently.",
        "🐱 The oldest known pet cat existed 9,500 years ago in Cyprus.",
        "🐱 Cats have over 30 muscles controlling their ears.",
        "🐱 A cat's heart beats twice as fast as a human's (110-140 bpm).",
        "🐱 Cats can jump up to 6 times their body length in a single bound!",
        "🐱 A cat's whiskers are roughly as wide as their body to help them navigate.",
        "🐱 Cats have a special reflective layer in their eyes called the 'tapetum lucidum'.",
        "🐱 The richest cat in the world inherited $13 million from its owner!",
        "🐱 Cats can make over 100 different sounds, while dogs only make about 10.",
        "🐱 A cat's brain is 90% similar to a human's brain!",
        "🐱 Cats don't have collarbones, which allows them to fit through any space their head can fit through.",
        "🐱 The first cat in space was French - her name was Félicette in 1963.",
        "🐱 Cats have scent glands on their paws, cheeks, and foreheads.",
        "🐱 A cat's tongue has tiny, hook-like structures that help them groom efficiently."
    ]
    
    print("🐱 Random Cat Fact of the Day: 🐱")
    print(random.choice(cat_facts))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--random":
        print_random_fact()
    else:
        print_cat_facts()
