block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    filtered_blocks = []
    for block in split_text:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_text(markdown):
    line_check = markdown.split("\n")
    heading_check = 0
    for i in range (7):
        if markdown[i] == "#":
            heading_check += 1
        elif markdown[i] == " ":
            break
        else:
            heading_check = 0
            break
    if heading_check != 0:
        return block_type_heading
    if len(line_check) > 1 and line_check[0].startswith("```") and line_check[-1].startswith("```"):
        return block_type_code
    quote = True
    u_list = True
    for i, line in enumerate(line_check):
        if line[0] != ">":
            quote = False
        if line[0] != "-" and line[0] != "*":
            u_list = False
    if quote == True:
        return block_type_quote
    if u_list == True:
        return block_type_ulist
    if markdown.startswith("1. "):
        i = 1
        for line in line_check:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
    

