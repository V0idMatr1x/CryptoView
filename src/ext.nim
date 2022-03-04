import nimpy


# Text Colors
proc red_text(text: string): string {.exportpy.} =
  return "[red]" & text


proc green_text(text: string): string {.exportpy.} =
  return "[green]" & text


proc purple_text(text: string): string {.exportpy.} =
  return "[purple]" & text


proc cyan_text(text: string): string {.exportpy.} =
  return "[cyan]" & text