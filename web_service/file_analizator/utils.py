import collections
import math
import os


def processing_file(file_path):
    words = get_words_from_file(file_path)
    tf_text = compute_tf(words)

    for key in tf_text:
        tf_text[key]['idf'] = compute_idf(key)
    sorted_tf_text = sort_dict_values(tf_text)
    return sorted_tf_text


def clean_text_and_create_array(text):
    trash_characters = ['(', ')', '{', '}', '\n', ',', ';', '.']
    for character in text:
        if character in trash_characters:
            text = text.replace(character, ' ')
    words_array = text.split(' ')
    words_array.remove('')
    return words_array


def sort_dict_values(tf_text):
    dict_with_idf = {}
    # create dict with only one key - word and one value - idf. It's simpler than sort source dict
    for key in tf_text:
        dict_with_idf[key] = tf_text[key]['idf']
    sorted_keys = sorted(tf_text, key=dict_with_idf.get, reverse=True)
    sorted_tf_text = {}
    i = 0
    for w in sorted_keys:
        if i == 50:
            break
        sorted_tf_text[w] = {}
        sorted_tf_text[w]['idf'] = tf_text[w]['idf']
        sorted_tf_text[w]['tf'] = tf_text[w]['tf']
        sorted_tf_text[w]['id'] = i + 1
        i += 1
    return sorted_tf_text


def get_words_from_file(file_path):
    folder = 'media/'
    file = open(folder + file_path)
    text = file.read()
    words = clean_text_and_create_array(text)
    return words


def compute_tf(words_array):
    tf_text = collections.Counter(words_array)
    words_characteristics = {}
    for i in tf_text:
        words_characteristics[i] = {}
        words_characteristics[i]['tf'] = tf_text[i] / float(len(words_array))
    return words_characteristics


def compute_idf(word):
    all_files = []
    # get all objects from dir
    path = os.getcwd()
    all_objects_in_media = os.scandir(path + '/media')
    # extract files from all objects
    for object_in_directory in all_objects_in_media:
        if object_in_directory.is_file():
            all_files.append(object_in_directory.name)

    array_of_words_from_all_files = []
    for file in all_files:
        file_words = get_words_from_file(file)
        array_of_words_from_all_files.append(file_words)
    return format(math.log10(len(array_of_words_from_all_files) /
                  sum([1.0 for i in array_of_words_from_all_files if word in i])), '.12f')
