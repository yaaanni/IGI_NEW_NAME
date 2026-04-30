# Purpose: Module containing text analysis classes, regex logic, and archiver mixins.
# Lab: #4 - Files, Classes, Serializers, Regular Expressions, and Standard Libraries.
# Version: 1.0.0.
# Developer: Popova Yana Georgievna.
# Date: 10.04.2026.

import re
import zipfile
import os
from abc import ABC, abstractmethod
from collections import Counter


class ZipArchiverMixin:
    """
    A mixin class providing functionality to archive files and read archive metadata.
    Demonstrates the use of mixins.
    """

    @staticmethod
    def archive_file(source_filepath: str, archive_filepath: str) -> None:
        """
        Compresses a specified file into a ZIP archive.

        Args:
            source_filepath (str): Path to the file to be compressed.
            archive_filepath (str): Path where the ZIP archive will be created.
        """
        try:
            with zipfile.ZipFile(archive_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(source_filepath, os.path.basename(source_filepath))
            print(f"[Archive OK] Result saved to archive: {archive_filepath}")
        except (IOError, zipfile.BadZipFile) as e:
            print(f"[Archive Error] Failed to create archive: {e}")

    @staticmethod
    def display_archive_info(archive_filepath: str) -> None:
        """
        Reads and prints metadata about the files contained within a ZIP archive.

        Args:
            archive_filepath (str): Path to the ZIP archive.
        """
        try:
            with zipfile.ZipFile(archive_filepath, 'r') as zipf:
                print("\n--- Archive Information ---")
                for info in zipf.infolist():
                    print(f"File Name: {info.filename}")
                    print(f"Original Size: {info.file_size} bytes")
                    print(f"Compressed Size: {info.compress_size} bytes")
                print("---------------------------\n")
        except (FileNotFoundError, zipfile.BadZipFile) as e:
            print(f"[Archive Error] Cannot read archive information: {e}")


class BaseTextAnalyzer(ABC):
    """
    Abstract base class for text analyzers.
    Demonstrates encapsulation, properties, and abstract methods.
    """

    def __init__(self, text: str):
        """Initializes the base analyzer."""
        self.text = text

    @property
    def text(self):
        """Getter for the text attribute."""
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """Setter for the text attribute."""
        if not isinstance(value, str):
            raise TypeError("Analyzed text must be a string.")
        if not value.strip():
            raise ValueError("Text cannot be empty.")
        self._text = value

    @abstractmethod
    def analyze(self) -> dict:
        """
        Abstract method to enforce polymorphism in child classes.
        Must return a dictionary containing analysis results.
        """
        pass


class VariantTextAnalyzer(BaseTextAnalyzer, ZipArchiverMixin):
    """
    Concrete analyzer implementing general and variant-specific text processing.
    Inherits from BaseTextAnalyzer and utilizes ZipArchiverMixin.
    """

    SMILEY_PATTERN = r'(?<![^\s])[:;]-*(?:\(+|\)+|\[+|\]+)(?![^\s.,!?])'
    VOWELS = "aeiouyаеёиоуыэюя"
    CONSONANTS = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"

    def __init__(self, text: str):
        """
        Initializes the Variant text analyzer using super().

        Args:
            text (str): The raw text to be analyzed.
        """
        super().__init__(text)

    def _analyze_general_requirements(self) -> dict:
        """Private method to process general lab requirements using RegEx."""

        sentences = re.findall(r'[^.!?]+[.!?]+', self.text)
        declarative = len(re.findall(r'[^.!?]+\.+', self.text))
        interrogative = len(re.findall(r'[^.!?]+\?+', self.text))
        exclamatory = len(re.findall(r'[^.!?]+!+', self.text))

        words = re.findall(r'\b[A-Za-zА-Яа-яЁё]+\b', self.text)
        total_words = len(words)
        all_letters = re.findall(r'[A-Za-zА-Яа-яЁё]', self.text)
        total_word_chars = len(all_letters)

        avg_word_len = round(total_word_chars / total_words, 2) if total_words else 0
        avg_sentence_len = round(total_word_chars / len(sentences), 2) if sentences else 0

        smileys = re.findall(self.SMILEY_PATTERN, self.text)

        return {
            "Total Sentences": len(sentences),
            "Declarative Sentences": declarative,
            "Interrogative Sentences": interrogative,
            "Exclamatory Sentences": exclamatory,
            "Average Word Length (chars)": avg_word_len,
            "Average Sentence Length (chars)": avg_sentence_len,
            "Total Smileys Found": len(smileys),
            "Smileys List": smileys
        }

    def _analyze_variant_requirements(self) -> dict:
        """Private method to process specific variant requirements using RegEx."""

        phones = re.findall(r'\b29\d{7}\b', self.text)

        pattern_2c_3v = fr'\b[A-Za-zА-Яа-яЁё][{self.CONSONANTS}{self.CONSONANTS.upper()}][{self.VOWELS}{self.VOWELS.upper()}][A-Za-zА-Яа-яЁё]*\b'
        words_2c_3v = re.findall(pattern_2c_3v, self.text)

        spaced_words = re.findall(r'(?<=\s)[A-Za-zА-Яа-яЁё]+(?=[.,!?]*\s)', self.text)

        counts = {}

        all_letters = re.findall(r'[a-zA-Zа-яА-ЯёЁ]', self.text)

        for letter in all_letters:
            is_already_counted = False
            for existing_key in counts.keys():
                if re.fullmatch(fr'{existing_key}', letter, flags=re.IGNORECASE):
                    is_already_counted = True
                    break

            if not is_already_counted:
                matches = re.findall(fr'{letter}', self.text, flags=re.IGNORECASE)
                counts[letter] = len(matches)

        phrases = re.findall(r'(?<=,)\s*([^,.!?\n\s][^,.!?\n]*[^,.!?\n\s])\s*(?=,)', self.text)
        phrases.sort()

        return {
            "Phones (29xxxxxxx)": phones,
            "Words (2nd Consonant, 3rd Vowel)": words_2c_3v,
            "Words strictly bounded by spaces count": len(spaced_words),
            "Letter Frequencies": counts,
            "Sorted Comma Phrases": phrases
        }

    def analyze(self) -> dict:
        """
        Main public method demonstrating polymorphism.
        Merges general and variant-specific results.

        Returns:
            dict: Combined dictionary of all text analysis metrics.
        """
        general_stats = self._analyze_general_requirements()
        variant_stats = self._analyze_variant_requirements()

        return {**general_stats, **variant_stats}

    def __str__(self) -> str:
        """Magic method providing a summary string representation."""
        return f"<VariantTextAnalyzer: Text Length = {len(self.text)} chars>"

    def __len__(self) -> int:
        """Magic method returning the length of the raw text."""
        return len(self.text)
